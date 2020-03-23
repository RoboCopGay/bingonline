from pages.models import *

users = [
    {
        'name': 'joao',
        'username': 'joao',
        'email': 'joao@j.com',
        'address': {
            'cep': '00000000',
            'city': 'zerada',
            'state': 'zero',
            'number': '00',
            'street': 'joao',
            'country': 'do cão',
            'neighborhood': 'inferno',
        },
        'password': 'joao123'
    },
    {
        'name': 'maria',
        'username': 'maria',
        'email': 'maria@j.com',
        'address': {
            'cep': '99998888',
            'city': 'belo boga',
            'state': 'fim de mundo',
            'number': '08',
            'street': 'maria',
            'country': 'do cão',
            'neighborhood': 'lula molusco',
        },
        'password': 'maria123'
    },
    {
        'name': 'joana',
        'username': 'joana',
        'email': 'joana@g.com',
        'address': 1,
        'password': 'morteaoshomens123'
    },
    {
        'name': 'joao roberto',
        'username': 'joaobeto',
        'email': 'joaobeto@docao.com',
        'address': 2,
        'password': 'joao123'
    },
    {
        'name': 'gabriel',
        'username': 'gabi',
        'email': 'gabi@j.com',
        'address': {
            'cep': '99998888',
            'city': 'belo boga',
            'state': 'fim de mundo',
            'number': '02',
            'street': 'maria',
            'country': 'do cão',
            'neighborhood': 'lula molusco',
        },
        'password': 'g4b1234'
    },
    {
        'name': 'ramires',
        'username': 'golias',
        'email': 'golias@boi.com',
        'address': {
            'cep': '99444488',
            'city': 'belo boga',
            'state': 'fim de mundo',
            'number': '75',
            'street': 'joana',
            'country': 'do cão',
            'neighborhood': 'fi do capeta',
        },
        'password': 'opirocudo'
    },
    {
        "name": "RoboCopGay daSilva",
        "username": "robocopgay",
        "email": "yaks.robocopgay@gmail.com",
        "password": "joao123",
        "address": {
            "cep": "99444488",
            "city": "belo boga",
            "state": "fim de mundo",
            "number": "75",
            "street": "joana",
            "country": "do cão",
            "neighborhood": "fi do capeta"
        }
    }
]


if __name__ == "__main__":
    for u in range(len(users)):
        print(':: Adding the <User> {\n',
              '\n'.join([ f'   {k}: {users[u][k]}\n' for k in users[u] ]), '}\n\n', sep='')
        users[u] = create_user(
            name=users[u]['name'],
            username=users[u]['username'],
            email=users[u]['email'],
            password=users[u]['password'],
            address=users[u]['address']
        )
