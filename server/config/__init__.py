from yaml import safe_load as yml
from os import environ as env

class _Conf:
    def __init__(self, c:dict):
        self.__dict__ = c

path = env['BINGONLINE_CONFIG'] if 'BINGONLINE_CONFIG' in env else env['HOME']+'/.config/bingonline.yml'
config = yml(path)
config = _Conf(config) if type(config)==dict else {
    # flask config
    'FLASK_APP': "app.py",
    'FLASK_ENV': "development",
    'FLASK_DEBUG': 1,
    'DB_PATH': "database.db",

    # mailbox config
    'EMAIL': '<email>',
    'password': '<password>',
    'SECRET_KEY': '<secret_key>',
    'SALT': '<salt_password>',
    'MAIL_SERVER': '<smtp>:<port>'
}
print(config.FLASK_APP)
