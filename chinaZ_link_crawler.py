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
from chinaZ_cache import ChianzCache

def chianz_link_crawler(seed_url,headers=None,proxy=None,user_agent='wswp',scrape_callback=0,cache=ChianzCache()):
    Num=0
    result=None
    crawl_queue=[]
    seen={seed_url:0}
    headers = headers or {}

    if user_agent:
        headers['User_agent'] = user_agent
    url = seed_url
    url_head=url[:-5]
    url_tile=url[-5:]
    for i in range(1,20):
        #depth = seen[url]
        depth = 0
        if i > 1:
            url = url_head + '_'+str(i)+url_tile
        result=dowload(url,headers=headers,proxy=proxy,data=None,num=Num,cache=None)#下载chinaZ 页面不计次数
        html=result['html']
        links=[]
        if scrape_callback:
            links.extend(scrape_callback(url, html) or [])
        links = get_links(html)
        for link in links:
            link = normalize( link)
            if link not in seen:
                seen[link]=depth+1
            crawl_queue.append(link)

    #while crawl_queue:
    for i in range(len(crawl_queue)):
        url = crawl_queue.pop()[0]
        result= dowload(url,headers=headers,proxy=proxy,num=i,data=None,cache=cache)
        html=result['html']
        result['url']=url                                            # 怎么把URL单独传进cache
        result['num']=i
        print(html)
        if cache:
            cache[i]=result

def dowload(url,headers,proxy,num,data=None,num_retries=2,cache=None):
    result=None
    code=0000
    html=''
    cache=cache
    if cache:
        try:
            record=cache[num]
            result=record['result']
            code=result['code']
            html=result['html']
            # if result['code']is not 200:
            #     result=None
        except KeyError:
            pass
            #result=None
    # else:
    #     if result['code'] is None or (num_retries > 0 and 500 <= result['code'] < 600):
    #         result = None
    if result is None:
        num += 1
        print(str(num)+'___Dowloading:'+url)
        request = urllib.request.Request(url,data,headers)
        opener = urllib.request.build_opener()
        html=''
        if proxy:
            proxy_params = {urlparse.urlparse(url).scheme: proxy}
            opener.add_handler(urllib.request.ProxyHandler(proxy_params))
        try:
            response = opener.open(request,timeout=60)
            html = response.read()
            code = response.code
        except urllib.error.HTTPError as e:
            if hasattr(e,'code'):
                code=e.code
                if num_retries > 0 and 500 <= code <= 600:
                     # retry 5xx errors
                    result = dowload(url, headers,proxy, num-1,data, num_retries - 1)
                    return result
            else:
                print(e)

        except urllib.error.URLError as e:
            print('Download error:', e.reason)
            html = ''
            if hasattr(e, 'code'):
                code = e.code
                if num_retries > 0 and 500 <= code <= 600:
                    # retry 5xx errors
                    result = dowload(url, headers,proxy,num-1, data, num_retries - 1)
                    return result
            else:
                print(e)
        except IOError as e:
            print(e)
        except Exception as e:
            print(e)
    return {'html': html, 'code': code}
    # if code == 200 or num_retries == 0:
    #     return {'html':html,'code':code}
    # else:
    #     return None

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
    chianz_link_crawler('http://top.chinaz.com/all/index.html')
    end = datetime.now()

    print(end - begin)