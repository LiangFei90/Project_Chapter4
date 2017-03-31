from datetime import datetime,timedelta
from pymongo import MongoClient

class ChianzCache:
    def __init__(self,client=None):
        self.client=MongoClient('localhost',27017) if client is None else client
        self.db=self.client.cache

    def __getitem__(self,num):
        record=self.db.chinaZ.find_one({'num':num})
        if record:
            return record
        else:
            raise KeyError('No.'+str(num)+' record does not exist')

    def __setitem__(self,num,  result):
        # record={'result':result,'timestamp':datetime.utcnow()}
        record = {'result': result}
        self.db.chinaZ.update({'num':num}, {'$set':record},upsert=True)