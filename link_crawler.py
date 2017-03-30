import urllib.request
import urllib.error
import urllib.parse
import urllib.robotparser as robotparser
import time
from datetime import datetime
import re
import types
# from CallBack import scrape_callback as  scrape_callback

def link_crawler(seed_url,link_regex=None,delay=2,max_depth=-1,max_urls=-1,headers=None,
                 user_agent='wswp',proxy=None,num_retries=-1,scrape_callback=0):
    """
    Crawl from the given seed url follwoing links matched by link_regex
    """
    crawl_quene=[seed_url]
    seen={seed_url:0}
    num_urls=0
    rp=get_robots(seed_url)
    print(rp)
    throttle=Throttle(delay)
    headers=headers or {}
    if user_agent:
        headers['User_agent']=user_agent
    while crawl_quene:
        url=crawl_quene.pop()
        depth=seen[url]
        if rp.can_fetch(user_agent,url):
            throttle.wait(url)
           # html=D(url)
            html=download(url,headers=headers,proxy=proxy,num_retries=2)
            links=[]
            if scrape_callback:
                links.extend(scrape_callback(url,html)or[])
            if depth != max_depth:
                if link_regex:
                    links.extend(link for link in get_links(html)if re.match(link_regex,link))

                    for link in links:
                        link = normalize(seed_url,link)
                        # check weather already crawled this link
                        if link not in seen:
                            seen[link]=depth+1
                            # check link is within same domain
                            if same_domain(seed_url,link):
                                # success! add this new link to quene
                                crawl_quene.append(link)
            # check weather have reached dowload maxnum
            num_urls+=1
            if num_urls==max_urls:
                break
        else:
            print('Blocked by robots.txt'+url)

class Throttle:
    """
    Add a delay between downloads to the same domian
    """
    def __init__(self,delay):
        self.delay=delay
        # timestamp of when a domain was last accessed
        self.domains={}
    def wait(self,url):
        domain=urllib.parse.urlparse(url).netloc
        last_accessed=self.domains.get(domain)

        if self.delay>0 and last_accessed is not None:
            sleep_sec=self.delay-(datetime.now()-last_accessed).seconds
            if sleep_sec>0:
                # domain has been accessed recently
                # so need to sleep
                time.sleep(sleep_sec)
            # update the lase accessed time
            self.domains[domain]=datetime.now()

def download(url,headers,proxy,num_retries,data=None):
    print('Downloading:',url)
    request=urllib.request.Request(url,data,headers)
    opener=urllib.request.build_opener()
    if proxy:
        proxy_params={urlparse.urlparse(url).scheme:proxy}
        opener.add_handler(urllib.request.ProxyHandler(proxy_params))
    try:
        response=opener.open(request)
        html=response.read()
        code=response.code
    except urllib.error.URLError as e:
        print ('Download error:',e.reason)
        html=''
        if hasattr(e,'code'):
            code=e.code
            if num_retries>0 and  500<=code <=600:
                # retry 5xx errors
                html=download(url,headers.proxy,num_retries-1,data)
            else:
                code=None
    return html

def normalize(seed_url,link):
    """
    Normalize this URL bu removing hash and adding domain
    """
    link,_=urllib.parse.urldefrag(link) # remove hash to avoid duplicates
    return urllib.parse.urljoin(seed_url,link)

def same_domain(url1,url2):
    """
    Return True if both URL's belong to same domain
    """
    return urllib.parse.urlparse(url1).netloc==urllib.parse.urlparse(url2).netloc

def get_robots(url):
    """
    Initialize robots parser for this domain
    """
    rp=robotparser.RobotFileParser()
    rp.set_url(urllib.parse.urljoin(url,'/robots.txt'))
    rp.read()
    return rp
def get_links(html):
    """
    Return a list of links from html
    """
    webpage_regex=re.compile('<a[^>]+href=["\'](.*?)["\']',re.IGNORECASE)
    #print (type(html))
    if type(html) is bytes:
        html=html.decode()
    elif type(html) is str:
        print(html)
    return webpage_regex.findall(html)

# def scrape_callback(url,html):
#     if re.search('/view/',url):
#         tree=lxml.html.fromstring(html)
#         row=[tree.cssselect('table>tr#places_%s__row>td.w2p_fw' % field)[0].text_content() for field in FIELDS]
#         print (url,row)

if __name__=='__main__':
    link_crawler('http://example.webscraping.com', '/(index|view)', delay=1, num_retries=1, user_agent='GoodCrawler')
    #CallBack.prt()