import urllib.request
import urllib.error
import urllib.parse
import time
import random
from datetime import datetime,timedelta
import socket

class Downloader:
    def __init__(self,user_agent='wswp',proxies=None,num_retries=1,timeout=60,opener=None,cache=None):
        socket.setdefaulttimeout(timeout)
        self.user_agent=user_agent
        self.proxies=proxies
        self.num_retries=num_retries
        self.opener=opener
        self.cache=cache
        #self.num=num

    def __call__(self,url,num):
        record=None
        if self.cache:
            try:
                record=self.cache[url]
                result=record['result']
                #print (result)
            except KeyError:
                pass
            else:
                if result['code'] is None or (self.num_retries > 0 and 500 <= result['code'] < 600):
                    record = None
        if record is None:
            #self.throttle.wait(url)
            proxy=random.choice(proxies ) if self.proxies else None
            headers={'User_agent':self.user_agent}
            print('No. '+str(num))
            result=self.download(url,headers,proxy,self.num_retries)
            if self.cache:
                # result['num']=num
                # record=result
                # resutl={'html':html,'code':code}
                record = {'result':result,'num':num}
                self.cache[url] = record
        return record

    def download(self,url,headers,proxy,num_retries,data=None,num=0):
        code=None
        html=''
        #num=record_num(num)
        print('   Downloading:',url)
        request=urllib.request.Request(url,data,headers or {})
        opener = urllib.request.build_opener()
        if proxy:
            proxy_params = {urlparse.urlparse(url).scheme:proxy}
            opener.add_handler(urllib.request.ProxyHandler(proxy_params))
        try:
            response=opener.open(request,timeout=60)
            html=response.read()
            code=response.code
        except urllib.error.HTTPError as e:
            if hasattr(e,'code'):
                code=e.code
                print('Download error:', e.reason)
                if num_retries > 0 and 500 <= code <= 600:
                     # retry 5xx errors
                    result = self.download(url,headers,proxy,num_retries-1,data)
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
                    result = self.download(url,headers,proxy,num_retries-1,data)
                    return result
            else:
                print(e)
        except IOError as e:
            print(e)
        except Exception as e:
            print ('Downloading Error :',str(e))
            html=''
            if hasattr(e,'code'):
                code=e.code
                if num_retries and 500<=code<600:
                    return self.download(url,headers,proxy,num_retries-1,data)
                else:
                    pass
                    # 修改此处，因为有时有些网页放回code 为403，若不记录此code,，返回空值，28行回报错
                    # code = None
        return {'html':html,'code':code}
def record_num(num):
    num += 1
    return num



