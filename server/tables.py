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

    address_id = db.Column(db.Integer, db.ForeignKey('Address.id'), nullable=False)
    address = db.relationship('Address', backref=db.backref(
        'residents', lazy=True
    ))

    def __repr__(self):
        return f'<User {self.email}>'

    def check_pass(self, passwd):
        return True if hash(passwd).hexdigest()==self.password else False

class Address(db.Model):
    __tablename__ = "Address"

    id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    cep = db.Column(db.String(8), nullable=False)
    city = db.Column(db.Text, nullable=False)
    state = db.Column(db.Text, nullable=False)
    number = db.Column(db.Text, nullable=False)
    street = db.Column(db.Text, nullable=False)
    country = db.Column(db.Text, nullable=False)
    complement = db.Column(db.Text, nullable=True)
    neighborhood = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Address {self.id}>'

class Event(db.Model):
    __tablename__ = "Event"

    id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)

    name = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text)
    fisic_ball = db.Column(db.Boolean, default=False)
    date = db.Column(db.DateTime, nullable=False)
    creation_date = db.Column(db.DateTime, nullable=False,
        default=datetime.utcnow)

class Prize(db.Model):
    __tablename__ = "Prize"

    id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    name = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=True)

    event_id = db.Column(db.Integer, db.ForeignKey('Event.id'), nullable=False)
    event = db.relationship('Event', backref=db.backref(
        'prizes', lazy=True
    ))

class Image(db.Model):
    __tablename__ = "Image"

    id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)

    alt = db.Column(db.Text, nullable=True)
    filename = db.Column(db.String(128), nullable=False)
    mime_type = db.Column(db.Text, nullable=False)

    prize_id = db.Column(db.Integer, db.ForeignKey('Prize.id'), nullable=False)
    prize = db.relationship('Prize', backref=db.backref(
        'images', lazy=True
    ))

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

