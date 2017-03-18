from urllib.request import urlopen
from urllib.parse import urlencode
import re

##wd=imput('输入一个要搜多的关键在:')
wd='python'
wd=urlencode({'wd':wd})
url='http://wwwd.baidu.com/s?'+wd
page=urlopen(url).read()
content=(page.decode('utf-8')).replace("\n","").replace("\t","")
title=re.findall(r'<h3 class="t".*h3>',cotent)
title=[item[item.find('href=')+6:item.find('target=')]for item in title]
title=[item.replace(' ','').replace('"','')for item in title]
for item in title:
    print(item)
