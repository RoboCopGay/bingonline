from database.models import *

data = {
    "name": "Bingo da neuza",
    "description": "bingo",
    "fisic_ball": False,
    "date": [2020, 6, 19, 14, 0]
}

create_event(
    name = data['name'],
    description = data['description'],
    date = data['date'],
    fisic_ball = data['fisic_ball'],
    owner = User.query.all()[0]
)

