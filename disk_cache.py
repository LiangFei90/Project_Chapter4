import os
import re
import urllib.parse
import pickle
from link_crawler_2 import link_crawler
import datetime

class DiskCache:
    def __init__(self,cache_dir='Caches'):
        self.cache_dir=cache_dir
        self.max_length=255

    def url_to_path(self,url):
        components=urllib.parse.urlsplit(url)
        path=components.path
        if not path:
            path='/index.html'
        elif path.endswith('/'):
            path+='index.html'
        filename=components.netloc+path+components.query
        filename=re.sub('[^/0-9a-zA-Z\-.,;_]','_',filename)
        filename='/'.join(segment[:255] for segment in filename.split('/'))
        return os.path.join(self.cache_dir,filename)

    def __getitem__(self,url):
        path=self.url_to_path(url)
        if  os.path.exists(path):
            with open(path,'rb') as fp:
                return pickle.load(fp)
        else:
            raise KeyError(url+'does not exist')

    def __setitem__(self,url,result):
        """
        save file to disk for this url
        """
        path =self.url_to_path(url)
        folder=os.path.dirname(path)
        if not os.path.exists(folder):
            os.makedirs(folder)                     # create flolader 'Caches\\example.webscraping.com'
        with open(path,'wb')as fp:             # path=Caches\\example.webscraping.com//index.html
            fp.write(pickle.dumps(result))

if __name__=='__main__':
    begin = datetime.datetime.now()
    link_crawler('http://example.webscraping.com/', '/(index|view)', cache=DiskCache())
    end = datetime.datetime.now()

    print(end-begin)