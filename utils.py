# https://www.oxfordstore.pe/bicicletas.html?limit=36&p=1
#    httpswww.oxfordstore.pebicicletas.htmllimit=36&p=1
def replace_chars_for_filename(url): 
    return url.replace(":","_")\
        .replace("/","_")\
        .replace("?","_")\
        .replace(".","_")\
        .replace("=","_")\
        .replace("&","_")

import urllib.parse

def extract_domain_from_url(url):
    return urllib.parse.urlparse(url).netloc

def ensure_absolute_url(base_url, url):
    return urllib.parse.urljoin(base_url, url) if url != "" else ""