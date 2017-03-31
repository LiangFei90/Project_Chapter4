import sys
from threaded_crawler import threaded_crawler
from MongoCache import MongoCache
from alexa_cb import AleaxCallBack

def main(max_threads):
    scrape_callback = AleaxCallBack()
    cache = MongoCache()
    threaded_crawler(scrape_callback.seed_url,scrape_callback=scrape_callback,
                     cache=cache,max_threads=max_threads,timeout=10)

if __name__=='__main__':
    #max_threads=int(sys.argv[1])
    max_threads=10
    main(max_threads)