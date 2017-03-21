import urllib.request
import urllib.error
import urllib.parse
import time
import random
from datetime import datetime,timedelta
import socket

class Downloader:
    def __init__(self,delay=5,user_agent='wswp',proxies=None,num_retries=1,timeout=60,opener=None,cache=None):
        socket.setdefaulttimeout(timeout)
        self.throttle=Throttle(delay)
        self.user_agent=user_agent
        self.proxies=proxies
        self.num_retries=num_retries
        self.opener=opener
        self.cache=cache

    def __call__(self,url):
        #print('It is __call__')
        result=None
        if self.cache:
            try:
                result=self.cache[url]
                #print (result)
            except KeyError:
                pass
            else:
                if self.num_retries > 0 and 500 <= result['code'] < 600:
                    result = None
        if result is None:
            self.throttle.wait(url)
            proxy=random.choice(proxies ) if self.proxies else None
            headers={'User_agent':self.user_agent}
            result=self.download(url,headers,proxy,self.num_retries)
            if self.cache:
                self.cache[url]=result                                                           # Create Foladers and caches and write caches
        return result['html']                                                                                 # MARK

    def download(self,url,headers,proxy,num_retries,data=None):
        code=None
        print('Downloading:',url)
        request=urllib.request.Request(url,data,headers or {})
        opener = urllib.request.build_opener()
        if proxy:
            proxy_params = {urlparse.urlparse(url).scheme:proxy}
            opener.add_handler(urllib.request.ProxyHandler(proxy_params))
        try:
            response=opener.open(request)
            html=response.read()
            #print('downloader_html:',html)
            code=response.code
        except Exception as e:
            print ('Downloading Error :',str(e))
            html=''
            if hasattr(e,'code'):
                code=e.code
                if num_retries and 500<=code<600:
                    return self._get(url,heasers,proxy,num_retries-1,data)
                else:
                    code = None
        return {'html':html,'coed':code}

class Throttle:
    def __init__(self,delay):
        self.delay=delay
        self.domain={}

    def wait(self,url):
        domain = urllib.request.urlsplit(url).netloc
        last_accessed=self.domain.get(domain)
        if self.delay>0 and last_accessed is not None:
            sleep_secs = self.delay-(datetime.now()-last_accessed.seconds)
            if sleep_secs > 0:
                tiem.sleep(sleep_secs)
            self.domain[domain]=datetime.now()

