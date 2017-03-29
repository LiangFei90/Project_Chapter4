import  csvImport
from alexa_cb import AleaxCallBack
from  link_crawler_4 import link_crawler
from MongoCache  import MongoCache

def main():
    scrape_callback=AleaxCallBack()
    link_crawler(seed_url=scrape_callback.seed_url,cache=MongoCache(),scrape_callback=scrape_callback,ignore_robots=True)

if __name__=='__main__':
    main()