import builtwith
import urllib.request
import urllib.error

def download(url,num_retries=2):
    print ('Downloading:',url)
    requst=urllib.request.Request(url)
    if hasattr(requst,'headers'):
            print(requst.headers)
    try:
        html=urllib.request.urlopen(url).read()
    except urllib.error.URLError as e:
        print('Downloading error:'+e.reason)
        html=None
        if num_retries>0:
            if hasattr(e,'code') and 500 <=e.code<600:
                return download(url,num_retries-1)
    return html
if __name__=='__main__':
    #print(download('http://meetup.com'))
    print(download('http://www.alexa.cn/siterank/1'))

