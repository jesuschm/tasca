import sys
import os.path
import configparser
from pathlib import Path

CONFIG_FILE = os.path.join(Path(__file__).parent.parent.parent, 'tasca.conf')


config = configparser.ConfigParser()

if os.path.isfile(CONFIG_FILE):
    print('[+] Loading config file tasca.conf')
    config.read([CONFIG_FILE])
else:
    print('[-] Config file not found. Quitting')
    sys.exit(1)
    
# mongodb settings
MONGO_HOST = config.get('mongodb', 'mongo_host')
MONGO_PORT = config.getint('mongodb', 'mongo_port')
MONGO_USER = config.get('mongodb', 'user')
MONGO_PASSWORD = config.get('mongodb', 'passwd')
MONGO_DB = config.get('mongodb', 'db')

MESSAGES_COLLECTION = config.get('mongodb', 'messages_collection')
USERS_COLLECTION = config.get('mongodb', 'users_collection')