import urllib.request
from urllib.parse import urlencode
import re
import io
import gzip

url='http://www.baidu.com/s?wd=python'

req=urllib.request.Request(url,headers={"Accept-Encoding": "gzip"})
                                                #headers={"Accept-Encoding": "gzip"有没有都行
page=urllib.request.urlopen(req).read()
bi=io.BytesIO(page)
#content=(page.decode('utf-8'))
gf=gzip.GzipFile(fileobj=bi,mode="rb")#百度网页经过GZIP压缩，需解压
#print(gf.read().decode("utf-8"))
ls=gf.read().decode("utf-8").replace("\n","").replace("\t","")
#print(ls)
title=re.findall(r'<h3 class="t".*?h3>',ls)
title=[item[item.find('href='):item.find('data-click=')]for item in title]

title=[item.replace(' ','').replace('"','')for item in title]
for item in title:
    print (item)

