from pages.models import *
from os import system as e
e('clear')

for i in [User, Board, Prize, Event]:
    print(i.__tablename__+':', end=' ')
    i = i.query.all()
    print(', '.join([ str(j) for j in i]))
    print()
