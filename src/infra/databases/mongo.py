from pymongo import MongoClient
from src.config.settings import MONGO_HOST, MONGO_PORT, MONGO_USER, MONGO_PASSWORD, MONGO_DB
from .repo import Repo
from src.config.settings import MESSAGES_COLLECTION

class MongoRepository(Repo):
    def __init__(self):
        self.client = self._get_client()
        
    def _get_client(self, host=MONGO_HOST, port=MONGO_PORT, user=MONGO_USER, password=MONGO_PASSWORD, db=MONGO_DB):
        try:
            uri = f"mongodb://"
            if user:
                uri += f"{user}:{password}@"
            uri += f"{host}:{port}/?authSource={db}"
            
            print ("[+] Connecting with the database...")
            client = MongoClient()
            client[db].command('ping')
            print ("[+] Successfully connected to the database.")
            return client
        except Exception:
            print(f'[-] Cannot instance connection with db.')
            return None
    
    def upsert(self, collection, data, pk_field):
        """Upsert method.

        Method to update or insert the data depending if the data already exists or not in the repository.

        Args:
            collection: collection name to update data.
            data: data to upsert.
            pk_field: field to be used to find the data to check if it already exists.

        """
        
        print('[+] Inserting/Updating data into %s collection.', collection)
        res = None

        try:
            res = self.client[MONGO_DB][collection].update({pk_field: data[pk_field]}, data, upsert=True)
            nUpserted= res['n']
            print(f'[+] Upserted {nUpserted} records in db.')
            res =  (nUpserted == 1)
        except Exception as err:
            print(f'[-] db_upsert: Cannot upsert data in db: {collection}. Error {err}.')
            
        return res
    
    def get(self, collection, filter, many, order_by, mode, limit, offset):
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
            print(f'[-] db_get: Cannot get data in db. Collection: {str(collection)} Filter: {str(filter)}')

        return res

    # Messages db actions
    def insert_message(self, message):
        return self.upsert(collection = MESSAGES_COLLECTION, data = message, pk_field = 'id')
    
    def get_messages(self, message):
        return self.get(collection= MESSAGES_COLLECTION, filter = filter, many = True, order_by = 'created_at', mode = 'desc')