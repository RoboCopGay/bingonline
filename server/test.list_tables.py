from models import *

for i in [User, Board, Address, Prize, Image, Event]:
    print(i.__tablename__+':', ', '.join(i.query.all()))
    print('\n')