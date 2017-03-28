import csv
from zipfile import ZipFile
from io import StringIO
from downloader import Downloader
import io
def alexa():
    D = Downloader()
    # zipped_data=D('http://s3.amazonaws.com/alexa-static/top-1m.csv.zip')
    zipped_data=D('http://localhost:8000/top-1m.csv.zip')
    print(type(zipped_data))
    urls=[] # top 1 million URL's will be stored in this list
    with ZipFile(io.BytesIO(zipped_data) ) as zf:
        print(type(zf))
        csv_filename=zf.namelist()[0]
        with open(csv_filename)as csvfile:
            for _, website in csv.reader(csvfile):
                 urls.append('http://'+website)
    # with open('top-1m.csv',newline='')as csvfile:
    #     for _,website in csv.reader(csvfile):
    #         urls.append('http://'+website)
    return urls
if __name__ == '__main__':

    urls=alexa()
    print(len(urls))
    for i in range(100):
        print(urls[i])
