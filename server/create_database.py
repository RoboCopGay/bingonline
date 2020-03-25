from database.models import *

if __name__ == "__main__":
    from app import db
    print(':: Creating tables of database')
    db.create_all()
