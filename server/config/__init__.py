from yaml import safe_load as yml
from os import environ as env

class _Conf:
    def __init__(self, c:dict):
        self.__dict__ = c

path = env['BINGONLINE_CONFIG'] if 'BINGONLINE_CONFIG' in env else env['HOME']+'/.config/bingonline.yml'
config = yml(path)
config = _Conf(config) if type(config)==dict else _Conf({
    # flask config
    'DB_PATH': "sqlite:///database.db",
    'SECRET_KEY': '<secret_key>',

    # mailbox config
    'EMAIL': '<email>',
    'EMAIL_PASS': '<password>',
    'SALT': '<salt_password>',
    'MAIL_SERVER': '<smtp>:<port>'
})
