from app import db

from hashlib import sha512 as hash


class User(db.Model):
    __tablename__ = "User"

    id = db.Column(db.Integer, primary_key=True, nullable=False)

    # username = db.Column(db.String(100))
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.String(128))

    def __repr__(self):
        return f'<User {self.email}>'

class Address(db.Model):
    __tablename__ = "Address"

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    cep = db.Column(db.String(8), nullable=False)
    city = db.Column(db.String(200), nullable=False)
    street = db.Column(db.String(200), nullable=False)
    neighborhood = db.Column(db.String(200), nullable=False)
    country = db.Column(db.String(200), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)
    user = db.relationship('User')

    def __repr__(self):
        return f'<Address {self.id}>'

class Phone(db.Model):
    __tablename__ = "Phone"

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    ddi = db.Column(db.String(4), default='+55')
    ddd = db.Column(db.String(3), nullable=False)
    digits = db.Column(db.String(10), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)
    user = db.relationship('User')

    def __repr__(self):
        return f'<Phone {self.ddi} ({self.ddd}) {self.digits})>'


def create_user(name, email, password):
    user = User(name=name, email=email, password=password)
    address = Address( cep='00000000', city='zero', street='zero', neighborhood='zero', country='zero', user=user)

    db.session.add(address)
    db.session.add(user)
    db.session.commit()

    return user

if __name__ == "__main__":
    print('Creating database...')
    db.create_all()
