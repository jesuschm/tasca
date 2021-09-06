import sys
import os.path
import configparser
import logging
import logging.config
from pathlib import Path

CONFIG_FILE = os.path.join(Path(__file__).parent.parent.parent, 'tasca.conf')

config = configparser.ConfigParser()

if os.path.isfile(CONFIG_FILE):
    logging.debug('[+] Loading config file tasca.conf')
    config.read([CONFIG_FILE])
else:
    logging.error('[-] Config file not found. Quitting')
    sys.exit(1)

# Set up a logger
LOG_CONFIG_FILE = os.path.join(Path(__file__).parent.parent.parent, 'logging.conf')

if os.path.isfile(LOG_CONFIG_FILE):
    logging.config.fileConfig(LOG_CONFIG_FILE)
    logger = logging.getLogger('tascalog')

# mongodb settings
MONGO_HOST = config.get('mongodb', 'mongo_host')
MONGO_PORT = config.getint('mongodb', 'mongo_port')
MONGO_USER = config.get('mongodb', 'user')
MONGO_PASSWORD = config.get('mongodb', 'passwd')
MONGO_DB = config.get('mongodb', 'db')

MESSAGES_COLLECTION = config.get('mongodb', 'messages_collection')
USERS_COLLECTION = config.get('mongodb', 'users_collection')