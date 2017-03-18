import lxml.html
from lxml import  etree
from lxml import  cssselect
import urllib.request
import urllib.error
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
html=download(url)
tree=lxml.html.fromstring(html)
td=tree.cssselect('tr#places_area__row>td.w2p_fw')[0]
area=td.text_content()
print(area)
# fixed_html=lxml.html.tostring(tree,pretty_print=True).decode()
# print (fixed_html)
