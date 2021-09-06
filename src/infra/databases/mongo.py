import logging
from pymongo import MongoClient
from src.config.settings import MONGO_HOST, MONGO_PORT, MONGO_USER, MONGO_PASSWORD, MONGO_DB, MESSAGES_COLLECTION, USERS_COLLECTION
from .repo import Repo

class MongoRepository(Repo):
    def __init__(self):
        self.client = self._get_client()
        
    def _get_client(self, host=MONGO_HOST, port=MONGO_PORT, user=MONGO_USER, password=MONGO_PASSWORD, db=MONGO_DB):
        try:
            uri = f"mongodb://"
            if user:
                uri += f"{user}:{password}@"
            uri += f"{host}:{port}/?authSource={db}"
            
            logging.debug("[+] Connecting with the database...")
            # uuidRepresentation = 'standard' helps mongo to manage uuid4 correctly.
            client = MongoClient(uuidRepresentation='standard') 
            client[db].command('ping')
            logging.debug("[+] Successfully connected to the database.")
            return client
        except Exception:
            logging.error(f'[-] Cannot instance connection with db.')
            return None
    
    def upsert(self, collection, data, pk_field):
        """Upsert method.

        Method to update or insert the data depending if the data already exists or not in the repository.

        Args:
            collection: collection name to update data.
            data: data to upsert.
            pk_field: field to be used to find the data to check if it already exists.

        """
        
        logging.debug('[+] Inserting/Updating data into %s collection.', collection)
        res = None

        try:
            res = self.client[MONGO_DB][collection].update({pk_field: data[pk_field]}, data, upsert=True)
            nUpserted= res['n']
            logging.debug(f'[+] Upserted {nUpserted} records in db.')
            res =  (nUpserted == 1)
        except Exception as err:
            logging.error(f'[-] db_upsert: Cannot upsert data in db: {collection}. Error {err}.')
            
        return res
    
    def get(self, collection, filter, many = False, order_by = None, mode = None, limit = 0, offset = 0):
        """Get data from the database. It removes by default the _id mongodb field.

        Args:
            collection: collection name.
            filter: filter to apply to database collection.
            many: to search more than one result
            order_by: field to sort
            mode: sorting mode (asc/desc)
            limit: number of elements to return
            offset: how many results are avoided in order to paginate the results

        Returns:
            response: post response in json format.

        """
        
        res = None

        try:
            if many:
                if order_by:
                    mode = 1 if mode == "asc" else -1 # By default, query is sorted desc.
                    res = self.client[MONGO_DB][collection].\
                        find(filter, {"_id": 0}).skip(offset).limit(limit).sort(order_by, mode)
                else:
                    res = self.client[MONGO_DB][collection].\
                        find(filter, {"_id": 0}).skip(offset).limit(limit)
            else:
                res = self.client[MONGO_DB][collection].find_one(filter, {"_id": 0})
                
        except Exception as err:
            logging.error(f'[-] db_get: Cannot get data in db. Collection: {str(collection)} Filter: {str(filter)}')

        return res

    # Messages db actions
    def insert_message(self, message):
        return self.upsert(collection = MESSAGES_COLLECTION, data = message, pk_field = 'id')
    
    def get_messages(self, user_ids):
        filter = { 
            'user_id' : { 
                '$in' : user_ids 
            } 
        }
        return self.get(collection= MESSAGES_COLLECTION, filter = filter, many = True, order_by = 'created_at', mode = 'desc')
    
    # Users db actions
    def create_user(self, user):
        return self._upsert_user(user)
    def update_user(self, user):
        return self._upsert_user(user)
    def _upsert_user(self, user):
        return self.upsert(collection= USERS_COLLECTION, data = user, pk_field = 'id')
    
    def get_user(self, username):
        filter = {
            'username': username
        }
        return self.get(collection= USERS_COLLECTION, filter = filter)

    def get_user_by_id(self, user_id):
        filter = {
            'id': user_id
        }        
        return self.get(collection= USERS_COLLECTION, filter = filter)