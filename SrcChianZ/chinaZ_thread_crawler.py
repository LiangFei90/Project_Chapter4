import threading
from chinaZ_downloader import  Downloader
from chinaZ_DBcache import ChianzCache
import time
from datetime import datetime
import types
import lxml.html
from lxml import  etree
from lxml import  cssselect
import urllib.request
import urllib.error
import urllib.parse


SLEEP_TIME=1

def threaded_crawler(seed_url,headers=None,proxy=None,user_agent='wswp',scrape_callback=0,cache=ChianzCache(),max_threads=10):
    crawl_queue=[seed_url]
    crawl_queue_links=[]
    links=[]

    D=Downloader(proxies=proxy,user_agent=user_agent,cache=cache)

    def process_queue_index():
        #while True:
        crawl_queue.pop()
        url = seed_url
        url_head = url[:-5]
        url_tile = url[-5:]
        # 爬取前20页的网页
        for i in range(1, 21):
            if i > 1:
                url = url_head + '_' + str(i) + url_tile
            record = D(url, num=0)
            result = record['result']
            html = result['html']
            links = get_links(html)
            for link in links:
                link = normalize(link)
                crawl_queue_links.append(link)

    def process_queue_link():
        # 下载队列里的网页
        # for j in range(1, len(crawl_queue_links) + 1):
        #     url = crawl_queue_links.pop()[0]
        #     #  record = D(url,num=j)
        #     D(url, num=j)
        # while True:
        try:
            url=crawl_queue_links.pop()[0]
        except IndexError:
            pass
        else:
            D(url,num)

    threads = []
    pool=[]
    num = 0
    while threads or crawl_queue or crawl_queue_links:

        # for i in range(len(threads)):
        #     if not threads[len(threads)-i].is_alive():
        #         threads.remove(threads[i])
        #         i -= 1
        while threads:
            thread=threads.pop()
            if thread.is_alive():
                pool.append(thread)
        threads.extend(pool)
        while len(threads) < max_threads and (crawl_queue or crawl_queue_links):
            if crawl_queue:
                thread = threading.Thread(target=process_queue_index())
                thread.setDaemon(True)
                thread.start()
                threads.append(thread)
            if crawl_queue_links:
                num+=1
                thread = threading.Thread(target=process_queue_link())
                thread.setDaemon(True)
                #print('__No.'+str(num))
                thread.start()
                threads.append(thread)
        time.sleep(SLEEP_TIME)

def get_links(html):
    links=[]
    tree = lxml.html.fromstring(html)
    spans= tree.cssselect('ul.listCentent span.col-gray')
    for i in range(len(spans)):
        url=spans[i].text_content()
        url='http://'+url
        links.append(url)
    return links

def normalize(link):
    """
    Normalize this URL bu removing hash and adding domain
    """
    link=urllib.parse.urldefrag(link) # remove hash to avoid duplicates
    return link

if __name__=='__main__':
    begin = datetime.now()
    threaded_crawler('http://top.chinaz.com/all/index.html')
    end = datetime.now()

    print(end - begin)