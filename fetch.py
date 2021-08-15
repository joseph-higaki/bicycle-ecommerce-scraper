import requests
import utils

HEADERS = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})    
            
def get_page_content(url):
    return dumb_cache(url)

# so that we don't shoot too many httprequests while testing
def dumb_cache(url):
    html_content = ""
    file_name = "page-cache/" + utils.replace_chars_for_filename(url)
    try:
        file = open(file_name,"r")
        html_content = file.read()
    except:        
        html_content = requests.get(url, headers=HEADERS).text
        file = open(file_name,"w")
        file.write(html_content)
        file.close()
    return html_content