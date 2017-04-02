import time
import threading
import urllib.parse
from downloader import Downloader

SLEEP_TIME=1

def threaded_crawler(seed_url,delay=5,cache=None,scrape_callback=None,user_agent='wswp',
                     proxies=None,num_retries=1,max_threads=10,timeout=60):
    """
    Crawl this website in multiple threads
    """
    crawl_queue = [seed_url]
    seen = set([seed_url])
    D = Downloader(cache=cache,delay=delay,user_agent=user_agent,proxies=proxies,num_retries=num_retries,
                   timeout=timeout)

    def process_queue():
        while True:
            try:
                url = crawl_queue.pop()
            except IndexError:
                break
            else:
                html=D(url)
                if scrape_callback:
                    try:
                        links=scrape_callback(url,html)or[]
                    except Exception as e:
                        print('Error in callback for:{}:{}'.format(url,e))
                    else:
                        for link in links:
                            #  link =normalize(seed_url,link)
                            if link not in seen:
                                seen.add(link)
                                crawl_queue.append(link)

    threads=[]
    while threads or crawl_queue:
        for thread in threads:
            if not thread.is_alive():
                threads.remove(thread)
        while len(threads)<max_threads and crawl_queue:
            thread = threading.Thread(target=process_queue())
            thread.setDaemon(True)
            thread.start()
            threads.append(thread)
        time.sleep(SLEEP_TIME)

    def normalize(seed_url,link):
        link,_ = urllib.parse.urldefrag(link)
        return urllib.parse.urlparse.urljoin(seed_url,link)