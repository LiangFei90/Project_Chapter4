import re
import urllib.request
import urllib.error
import urllib.parse


def link_crawler(seed_url, link_regex):
    crawl_queue = [seed_url]
    seen = set(crawl_queue)
    while crawl_queue:
        url = crawl_queue.pop()  # pop()66666666
        # print(url)
        html = download(url)
        for link in get_links(html):
            # print('link is : ' +link)
            if re.match(link_regex, link):
                link = urllib.parse.urljoin(seed_url, link)
                if link not in seen:
                    seen.add(link)
                    crawl_queue.append(link)
                    print('Downloading: ' + link)


def get_links(html):
    webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
    # print( webpage_regex )
    html = html.decode()
    return webpage_regex.findall(html)


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


if __name__ == '__main__':
    link_crawler('http://example.webscraping.com', '/(view|index)')
