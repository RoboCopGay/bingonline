from app import db
from datetime import datetime

class User(db.Model):
    __tablename__ = "User"

    id = db.Column(db.Integer, primary_key=True, nullable=False,  unique=True)

    name = db.Column(db.Text)
    email = db.Column(db.Text, unique=True)
    phone = db.Column(db.String(12), unique=True)

    username = db.Column(db.Text, unique=True)
    password = db.Column(db.String(128))

    creation_date = db.Column(db.DateTime, nullable=False,
        default=datetime.utcnow)
    alter_date = db.Column(db.DateTime, nullable=False,
        default=datetime.utcnow)

    perfil = db.Column(db.String(128), nullable=True)
    address = db.Column(db.JSON, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

    def check_pass(self, passwd):
        return True if hash(bytes(passwd, 'utf-8')).hexdigest()==self.password else False

class Event(db.Model):
    __tablename__ = "Event"

    id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)

    name = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text)
    fisic_ball = db.Column(db.Boolean, default=False)
    date = db.Column(db.DateTime, nullable=False)
    creation_date = db.Column(db.DateTime, nullable=False,
        default=datetime.utcnow)

    def __repr__(self):
        return f'<Event {self.name}>'

class Prize(db.Model):
    __tablename__ = "Prize"

    id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    name = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=True)

    images = db.Column(db.JSON, nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('Event.id'), nullable=False)
    event = db.relationship('Event', backref=db.backref(
        'prizes', lazy=True
    ))

    def __repr__(self):
        return f'<Prize {self.name}>'

class Board(db.Model):
    __tablename__ = "Board"

    id = db.Column(db.Integer, primary_key=True, nullable=False,  unique=True)

    values = db.Column(db.JSON(), nullable=False, unique=True)

    user_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)
    user = db.relationship('User', backref=db.backref(
        'boards', lazy=True
    ))
    event_id = db.Column(db.Integer, db.ForeignKey('Event.id'), nullable=False)
    event = db.relationship('Event', backref=db.backref(
        'boards', lazy=True
    ))

    def __repr__(self):
        return f'<Board {self.id}>'

def generate_board() -> list:
    def do_sort():
        history = []
        width, height = 5, 5
        values = [[ 0 for j in range(height)] for i in range(width)]

        bingo = [
            [ 1, 15], # B
            [16, 30], # I
            [31, 45], # N
            [46, 60], # G
            [61, 75]  # O
        ]

        for i in range(width):
            for j in range(height):
                sort = randint(bingo[j][0], bingo[j][1])
                while sort in history:
                    sort = randint(1, 75)
                values[i][j] = sort
                history.append(sort)
        values[2][2] = 0
        return values

    values = do_sort()
    history = [ b.values for b in Board.query.all()]
    while values in history:
        values = do_sort()
    return values
