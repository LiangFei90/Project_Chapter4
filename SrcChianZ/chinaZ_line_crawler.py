import urllib.request
import urllib.error
import urllib.parse
import urllib.robotparser as robotparser
import time
from datetime import datetime
import re
import types
import lxml.html
from lxml import  etree
from lxml import  cssselect
from chinaZ_DBcache import ChianzCache
from chinaZ_downloader import Downloader

def chinaz_line_crawler(seed_url,headers=None,proxy=None,user_agent='wswp',scrape_callback=0,cache=ChianzCache()):
    crawl_queue=[]
    links=[]
    headers=headers or {}
    D=Downloader(proxies=proxy,user_agent=user_agent,cache=cache)
    if user_agent:
        headers['User_agent'] = user_agent
    # 把url切割，方便加入序号
    url = seed_url
    url_head = url[:-5]
    url_tile = url[-5:]
    # 爬取前20页的网页
    for i in range(1,21):
        if i >1:
            url=url_head+'_'+str(i)+url_tile
        record=D(url,num=0)
        result=record['result']
        html= result['html']
        links = get_links(html)
        for link in links:
            link = normalize(link)
            crawl_queue.append(link)

    #下载队列里的网页
    for j in range(1,len(crawl_queue)+1):
        url = crawl_queue.pop()[0]
        #  record = D(url,num=j)
        D(url,num=j)
       # html= resutl['html']
       # code=result['code'] if result['code'] is not None
       #  if cache:
       #      cache[url]=record

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
    chinaz_line_crawler('http://top.chinaz.com/all/index.html')
    end = datetime.now()

    print(end - begin)