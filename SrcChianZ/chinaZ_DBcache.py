from datetime import datetime,timedelta
from pymongo import MongoClient

class ChianzCache:
    def __init__(self,client=None):
        self.client=MongoClient('localhost',27017) if client is None else client
        self.db=self.client.cache

    def __getitem__(self,url):
        record=self.db.chinaZ02.find_one({'url':url})
        if record:
            return record
        else:
            raise KeyError(url,'record does not exist')

    def __setitem__(self,url,  record):
        # record={'result':result,'timestamp':datetime.utcnow()}
        #num = record['num']
        #del record['num']
        #insertrecord = {'result': record,'num':num}
        self.db.chinaZ02.update({'url':url}, {'$set':record},upsert=True)