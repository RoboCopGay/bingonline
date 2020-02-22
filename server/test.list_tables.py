from models import *

for i in [User, Board, Prize, Event]:
    print(i.__tablename__+':', ', '.join(i.query.all()))
    print('\n')
