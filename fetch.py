#from my_scraper import MyScraper
import config 
import requests
from requests.api import get
import utils

import time
from selenium import webdriver

USE_CACHE = False
HEADERS = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})    
            
def get_page_content(url, force_bottom_scroll = False):
    return_value = ""
    use_cache = USE_CACHE 
    if use_cache:
        return_value = _dumb_cache(url, force_bottom_scroll)
    else: 
        return_value = _get_page_response_content(url, HEADERS, force_bottom_scroll)
    return return_value

# so that we don't shoot too many httprequests while testing
def _dumb_cache(url, force_bottom_scroll = False):
    html_content = ""
    file_name = "page-cache/" + utils.replace_chars_for_filename(url)
    try:
        file = open(file_name,"r", encoding="utf-8")
        html_content = file.read()
    except:                
        html_content = _get_page_response_content(url, HEADERS, force_bottom_scroll)
        file = open(file_name,"w", encoding="utf-8")
        file.write(html_content)
        file.close()
    return html_content

def _get_page_response_content(url, headers, force_bottom_scroll = False):
    returnValue = ""
    if force_bottom_scroll:
        returnValue = get_dynamic_page_content_bottom_scroll_instantiating_driver(url)
    else:
        returnValue = requests.get(url, headers=HEADERS).text     
    return returnValue

def get_browser():
    options = webdriver.FirefoxOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')    
    #options.set_headless()                       
    driver = webdriver.Firefox(executable_path="./browser-driver/geckodriver.exe", firefox_options = options)
    return driver

def scroll_to_bottom(driver):
    screen_height = driver.execute_script("return window.screen.height;")
    ##### Web scrapper for infinite scrolling page #####
    time.sleep(config.Config().get_global_attribute("initial_load_sleep"))  # Allow 2 seconds for the web page to open
    scroll_pause_time = 1 # You can set your own pause time. My laptop is a bit slow so I use 1 sec
    i = 1
    while True:
        # scroll one screen height each time
        driver.execute_script(f"window.scrollTo(0,{screen_height * i});")
        i += 1
        time.sleep(config.Config().get_global_attribute("after_scroll_sleep"))
        # update scroll height each time after scrolled, as the scroll height can change after we scrolled the page
        scroll_height = driver.execute_script("return document.body.scrollHeight;")  
        # Break the loop when the height we need to scroll to is larger than the total scroll height
        if (screen_height) * i > scroll_height:
            break 

def get_dynamic_page_content_bottom_scroll(url, driver):
    driver.get(url)
    scroll_to_bottom(driver)
    return_value = driver.page_source
    return return_value

def get_dynamic_page_content_bottom_scroll_instantiating_driver(url):
    return_value = ""
    driver = get_browser()
    try:
        get_dynamic_page_content_bottom_scroll(url, driver)
    finally:
        driver.close()
    return return_value