import urllib.request
response=urllib.request.urlopen('http://www.baidu.com/s?+python')
html=response.read().decode('utf-8')
print(html)
