# https://www.oxfordstore.pe/bicicletas.html?limit=36&p=1
#    httpswww.oxfordstore.pebicicletas.htmllimit=36&p=1
def replace_chars_for_filename(url): 
    return url.replace(":","_")\
        .replace("/","_")\
        .replace("?","_")\
        .replace(".","_")\
        .replace("=","_")\
        .replace("&","_")

from urllib.parse import urlparse
def extract_domain_from_url(url):
    urlparse(url).netloc