import csv
from zipfile import ZipFile
import io
from MongoCache import MongoCache


class AleaxCallBack:
    def __init__(self, max_urls=1000):
        self.max_urls = max_urls
        # self.seed_url='http://s3.amazonaws.com/alexa-static/top-1m.csv.zip'
        self.seed_url = 'http://localhost:8080/top-1m.csv.zip'

    def __call__(self, url, html):
        if url == self.seed_url:
            urls = []
            cache = MongoCache()
            with ZipFile(io.BytesIO(html))as zf:
                csv_filename = zf.namelist()[0]
                for _, website in csv.reader(open(csv_filename)):
                    # if 'http://'+website not in cache:
                    urls.append('http://' + website)
                    if len(urls) == self.max_urls:
                        break
            return urls
            # urls=[]
            # cache=MongoCache()
            # with open('top-1m.csv',newline='') as csvfile:
            #     for _,website in csv.reader(csvfile):
            #          if  'http://'+website not in cache:
            #
            #             urls.append('http://'+website)
            #             if len(urls)==self.max_urls:
            #                 break
            # return urls
