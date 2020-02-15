from hashlib import sha512 as hash
from random import randint
from re import search

from tables import *

# Game
def generate_board():
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

def create_board(user, event):
    board = Board(user=user, event=event)
    board.values = generate_board()

    db.session.add(board)
    db.session.commit()

    return board

# User
def create_address(cep, number, street, neighborhood, city, state, country):
    address = Address(
        cep=cep,
        city=city,
        state=state,
        street=street,
        number=number,
        country=country,
        neighborhood=neighborhood
    )

    db.session.add(address)
    db.session.commit()

    return address

def create_user(name, username, email, password, address):
    user = User(name=name, username=username, email=email, password=password, address=address)

    db.session.add(user)
    db.session.commit()

    return user

if __name__ == "__main__":
    print('Creating tables of database...')
    db.create_all()
