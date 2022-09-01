import configparser

config = configparser.ConfigParser()
print(config.read('config.ini'))

print('Sections:', config.sections(), '\n')

print('mariadb sections:')
print('Host:', config['mariadb']['host'])
print('Database:', config['mariadb']['name'])
print('Username:', config['mariadb']['user'])
print('Password:', config['mariadb']['password'])

print('redis section:')
print('Host:', config.get('redis', 'host'))
print('Port:', config.get('redis', 'port'))
print('Database number:', config.get('redis', 'db'))
print('dsn:', config.get('redis', 'dsn'))
