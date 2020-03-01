from hashlib import sha512 as hash
from random import randint
from re import search

from tables import *

# Game
def create_board(user:User, event:Event) -> Board:
    board = Board(
        user=user,
        event=event
    )
    board.values = generate_board()

    db.session.add(board)
    db.session.commit()

    return board

def create_event(name:str, date:tuple, owner:User, description:str = None, fisic_ball:str = False) -> Event:
    year, month, day, hour, minute = date
    event = Event(
        name=name,
        description=description,
        date=datetime(year, month, day, hour, minute),
        fisic_ball=fisic_ball,
        owner=owner
    )

    db.session.add(event)
    db.session.commit()

    return event

def create_prize(name:str, description:str, images:dict, event:Event) -> Prize:
    prize = Prize(
        name=name,
        description=description,
        event=event,
        images=images
    )

    db.session.add(prize)
    db.session.commit()

    return prize

# User
def create_user(name:str, username:str, email:str, password:str, address:dict) -> User:
    user = User(
        name=name,
        username=username,
        email=email,
        password=hash(bytes(password, 'utf-8')).hexdigest(),
        address=address
    )

    db.session.add(user)
    db.session.commit()

    return user

