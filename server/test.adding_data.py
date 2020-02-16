from models import *

users = [
    {
        'name': 'joao',
        'username': 'joao',
        'email': 'joao@j.com',
        'address': 0,
        'password': b'joao123'
    },
    {
        'name': 'maria',
        'username': 'maria',
        'email': 'maria@j.com',
        'address': 0,
        'password': b'maria123'
    },
    {
        'name': 'joana',
        'username': 'joana',
        'email': 'joana@g.com',
        'address': 1,
        'password': b'morteaoshomens123'
    },
    {
        'name': 'joao roberto',
        'username': 'joaobeto',
        'email': 'joaobeto@docao.com',
        'address': 2,
        'password': b'joao123'
    },
    {
        'name': 'gabriel',
        'username': 'gabi',
        'email': 'gabi@j.com',
        'address': 2,
        'password': b'g4b1234'
    },
    {
        'name': 'ramires',
        'username': 'golias',
        'email': 'golias@boi.com',
        'address': 3,
        'password': b'opirocudo'
    }
]

addresses = [
    {
        'cep': '00000000',
        'city': 'zerada',
        'state': 'zero',
        'number': '00',
        'street': 'joao',
        'country': 'do cão',
        'neighborhood': 'inferno',
    },
    {
        'cep': '99998888',
        'city': 'belo boga',
        'state': 'fim de mundo',
        'number': '08',
        'street': 'maria',
        'country': 'do cão',
        'neighborhood': 'lula molusco',
    },
    {
        'cep': '99998888',
        'city': 'belo boga',
        'state': 'fim de mundo',
        'number': '02',
        'street': 'maria',
        'country': 'do cão',
        'neighborhood': 'lula molusco',
    },
    {
        'cep': '99444488',
        'city': 'belo boga',
        'state': 'fim de mundo',
        'number': '75',
        'street': 'joana',
        'country': 'do cão',
        'neighborhood': 'fi do capeta',
    }
]

if __name__ == "__main__":
    for a in range(len(addresses)):
        print(':: Adding the <Address> {\n',
              '\n'.join([ f'   {k}: {addresses[a][k]}' for k in addresses[a] ]), '}\n\n', sep='')
        addresses[a] = create_address(
            cep=addresses[a]['cep'],
            city=addresses[a]['city'],
            state=addresses[a]['state'],
            number=addresses[a]['number'],
            street=addresses[a]['street'],
            country=addresses[a]['country'],
            neighborhood=addresses[a]['neighborhood']
        )
    for u in range(len(users)):
        print(':: Adding the <User> {\n',
              '\n'.join([ f'   {k}: {users[u][k]}\n' for k in users[u] ]), '}\n\n', sep='')
        users[u] = create_user(
            name=users[u]['name'],
            username=users[u]['username'],
            email=users[u]['email'],
            password=users[u]['password'],
            address=addresses[users[u]['address']]
        )
