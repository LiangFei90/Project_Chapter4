from datetime import datetime,timedelta
from pymongo import MongoClient
from link_crawler_2 import link_crawler
class MongoCache:
    def __init__(self,client=None,expires=timedelta(days=30)):
        self.client=MongoClient('localhost',27017) if client is None else client
        self.db=self.client.cache
        #self.db.webpage.create_index({'timestamp':1},{expireAfterSeconds:expires.total_seconds()})

    def __getitem__(self,url):
        record=self.db.webpage01.find_one({'_id':url})
        if record:
            return record['result']
        else:
            raise KeyError(url+'does not exist')

    def __setitem__(self, url, result):
        #record={'result':result,'timestamp':datetime.utcnow()}
        record = {'result': result}
        self.db.webpage01.update({'_id':url},{'$set':record},upsert=True)

if __name__=='__main__':
    begin = datetime.now()
    link_crawler('http://example.webscraping.com/', '/(index|view)', cache=MongoCache(expires=timedelta()))
    end = datetime.now()

    print(end-begin)