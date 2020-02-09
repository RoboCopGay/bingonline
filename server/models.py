from app import db

from hashlib import sha512 as hash


class Phone(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    ddi = db.Column(db.String(4), default='+55')
    ddd = db.Column(db.String(3), nullable=False)
    digits = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return f'<Phone {self.ddi} ({self.ddd}) {self.digits})>'


class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    cep = db.Column(db.String(8), nullable=False)
    city = db.Column(db.String(200), nullable=False)
    street = db.Column(db.String(200), nullable=False)
    neighborhood = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<Address {self.id}>'

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)

    username = db.Column(db.String(100))
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.String(128))


    address_id = db.Column(db.Integer, db.ForeignKey('Address.id'), nullable=False)
    phone_id = db.Column(db.Integer, db.ForeignKey('Phone.id'), nullable=True)

    address = db.relationship('Address')
    phone = db.relationship('Phone')

    def __repr__(self):
        return f'<User {self.username}>'


def create_user(name, email, password, address_id, phone_id=None):
    user = User(name, email, password, address_id, phone_id)

    db.session.add(user)
    db.session.commit()

    return user

if __name__ == "__main__":
    print('Creating database...')
    db.create_all()
