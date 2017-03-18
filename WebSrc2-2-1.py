from bs4 import BeautifulSoup
import urllib.request
import urllib.error
# broken_html = '<ul class=\'country\'><li>Area</li><li>Population</ul>'
# soup = BeautifulSoup(broken_html,'html.parser')
# fixed_html = soup.prettify()
# #print(fixed_html)
#
# ul = soup.find('ul',attrs={'class':'country'})
#
# fin = ul.find('li')
# fins = ul.find_all('li')
# print(fin)
# print(fins)
def download(url,user_agent='wswp',proxy=None,num_retries=2):
    # print('Donwloading: '+url)
    headers = {'User_agent':user_agent}
    # num_retries = 2
    request = urllib.request.Request(url,headers=headers)
    opener=urllib.request.build_opener()
    if proxy:
        proxy_params = {urllib.urlparse.urlparse(url).scheme:proxy}
        opener.add_handler(urllib.request.ProxyHandler(proxy_params))

    try:
        html = opener.open(request).read()
    except urllib.error.URLError as e:
        print('Downloading error:', e.reason)
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                return download(url, user_agent,proxy, num_retries - 1)
    return html
url = 'http://example.webscraping.com/places/view/United-Kindom-239'
html = download(url)
soup = BeautifulSoup(html,'html.parser')
tr = soup.find(attrs={'id':'places_area__row'})
td = tr.find(attrs={'class':'w2p_fw'})
area = td.text
print(area)
