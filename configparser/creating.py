import configparser

config = configparser.ConfigParser()

config['DEFAULT'] = {'host': 'localhost'}
config['martiadb'] = {
    'name': 'hello',
    'username': 'root',
    'password': 'password'
}
config['redis'] = {
    'port': 6379,
    'db': 0
}

with open('config_2.ini', 'w') as configfile:
    config.write(configfile)