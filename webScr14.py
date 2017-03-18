import urllib.request
import urllib.error
import itertools

max_errors=5
num_errors=0

def download(url):
    #print ('Downloading:',url)
    #headers={'User-agent':user_agent}
    num_retries=2
    requst=urllib.request.Request(url)
    try:
        html=urllib.request.urlopen(url).read()
    except urllib.error.URLError as e:
        print('Downloading error:',e.reason)
        html=None
        if num_retries>0:
            if hasattr(e,'code') and 500 <=e.code<600:
                return download(url,user_agent,num_retries-1)
    return html

for page in itertools.count(1):
    url='http://example.webscraping.com/view/-%d'%page
    html=download(url)
    if html is None:
        num_errors+=1
        if num_errors==max_errors:
            break
    else:
        print(url)
        num_errors=0


#if __name__=='__main__':
#    download('http://www.meetup.com')
