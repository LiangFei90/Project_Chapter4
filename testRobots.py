import urllib.robotparser as  robotparser
import urllib.parse

def get_robots(url):
    """
    Initialize robots parser for this domain
    """
    rp=robotparser.RobotFileParser()
    rp.set_url(urllib.parse.urljoin(url,'/robots.txt'))
    rp.read()
    print(rp)
seed_url='http://example.webscraping.com'
get_robots(seed_url)