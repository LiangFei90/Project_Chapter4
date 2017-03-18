import urllib.request
import urllib.error
import re
import urllib.parse
import urlparse
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
        self.num_retires=num_retries
        self.opener=opener
        self.cache=cache

    def __call__(self,url):
        result=None
        if self.catch:
            try:
                result=self.catch[url]
            except KeyError:
                pass
        else:
            if self.num_retires>0 and 500<=result['code']<600:
                result=None
        if result is None:
            self.throttle.wait(url)
            proxy=random.choice(proxies ) if self.proxies else None
            headers={'User_agent':self.user_agent}
            result=self.download(url,headers,proxy,self.num_retries)
            if self.cache:
                self.cache[url]=result

    def download(self,heasers,proxy,num_retries):
        print('Downloading:'url)
        request=urllib.request.Request(url.data.handers or {})
        opener = urllib.request.build_opener()
        if proxy:
            proxy_params = {urlparse.urlparse(url).scheme:proxy}
            opener.add_handler(urllib.request.ProxyHandler(proxy_params))
        try:
            response=opener.open(request)
            html=response.read()
            code=response.code
        except Exception as e:
            print ('Downloading Error :'str(e))
            html=''
            if hasattr(e,'code'):
                code=e.code
                if num_retries and 500<=code<600:
                    return self._get(url,heasers,proxy,num_retries-1,data)
                else:
                    code = None
        return {'html':html,'code':code}

class Throttle:
    def __init__(self,delay):
        self.delay=delay
        self.domain={}
    def wait(self,url):
        domain = urlparse.urlsplit(url).netloc
        last_accessed=self.domain.get(domain)
        if self.delay>0 and last_accessed is not None:
            sleep_secs = self.delay-(datatime.now()-last_accessed.seconds)
            if sleep_secs > 0:
                tiem.sleep(sleep_secs)
            self.domain[domain]=datatime.now()

