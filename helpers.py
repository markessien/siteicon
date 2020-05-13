
from urllib.parse import urljoin

def fully_qualify_url(base_url, the_url):
    return urljoin(base_url, the_url)