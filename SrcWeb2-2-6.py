import lxml.html
import urllib.request
import urllib.error
import re
from  webScr16 import download as  download
#from link_crawler import link_crawler
FIELDS = ('area', 'population', 'iso', 'country', 'capital', 'continent', 'tld', 'currency_code', 'currency_name', 'phone', 'postal_code_format', 'postal_code_regex', 'languages', 'neighbours')
def scrape_callback(url,html):
    if re.search('/view/',url):
        tree=lxml.html.fromstring(html)
        row = [tree.cssselect('table>tr#places_%s__row>td.w2p_fw'%field)[0].text_content()for field in FIELDS]
        print (url)
        for item in row:
            print (item)




if __name__=='__main__':
    url='http://example.webscraping.com/places/view/United-Kindom-239'
    html=download(url)
    links=[]
   # link_crawler('http://example.webscraping.com','/(index|view)',scrape_callback)
    links.extend(scrape_callback(url,html)or [])