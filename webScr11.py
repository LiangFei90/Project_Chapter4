import builtwith
import urllib.request
import urllib.error

def download(url,user_agent='Python-urllib/2.7',num_retries=2):
    print ('Downloading:',url)
    headers={'User-agent':user_agent}
    requst=urllib.request.Request(url,headers=headers)
    try:
        html=urllib.request.urlopen(url).read()
    except urllib.error.URLError as e:
        print('Downloading error:',e.reason)
        html=None
        if num_retries>0:
            if hasattr(e,'code') and 500 <=e.code<600:
                return download(url,user_agent,num_retries-1)
    return html
if __name__=='__main__':

   html=download('http://www.meetup.com')
   print(html)