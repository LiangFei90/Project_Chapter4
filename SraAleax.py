import lxml.html
from lxml import  etree
from lxml import  cssselect
import urllib.request
import urllib.error
import urllib.parse
def download(url,user_agent='BadCrawler',proxy=None,num_retries=2):
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

# url = 'http://example.webscraping.com/places/view/United-Kindom-239'
url='http://top.chinaz.com/all/index.html'
html=download(url)
#print(html)
tree=lxml.html.fromstring(html)
print(type(tree))
print(len(tree))
print(tree[0])
print(tree[1].tag)

# td=tree.cssselect('tr#places_area__row>td.w2p_fw')[0]
# area=td.text_content()
# print(area)

span=tree.cssselect('ul.listCentent span.col-gray')[0]
print(len(span))
print(span.text_content())
result=urllib.parse.urlsplit(url)
print(result)
print(url[:-5])
print(url[-5:])

#fixed_html=lxml.html.tostring(tree,pretty_print=True).decode()
#print (fixed_html)
