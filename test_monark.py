#import sys
#sys.path.append('../')

from scraper_type import ScraperType
import pytest 
from lxml import html
from my_scraper import MyScraper


@pytest.fixture
def html_static_content_first_page():
    return open("tests/test_data/https___www_monark_com_pe_categoria-producto_bicicletas_","r", encoding="utf-8").read()

@pytest.fixture
def html_static_content_last_page():
    return open("tests/test_data/https___www_monark_com_pe_categoria-producto_bicicletas__page_6","r", encoding="utf-8").read()

@pytest.fixture
def monark_scraper_type():
    return ScraperType.create_scraper_type("monark.com.pe")

@pytest.fixture
def monark_scraper(monark_scraper_type):
    return MyScraper(monark_scraper_type)

@pytest.fixture
def product_list_first_page(monark_scraper, html_static_content_first_page):    
    html_tree = html.fromstring(html_static_content_first_page)    
    return monark_scraper.get_product_element_list(html_tree)   

@pytest.fixture
def product_list_last_page(monark_scraper, html_static_content_last_page):    
    html_tree = html.fromstring(html_static_content_last_page)    
    return monark_scraper.get_product_element_list(html_tree)   

@pytest.fixture
def product_liv_bliss_275_eclipse(monark_scraper, product_list_first_page):
    # BICICLETA LIV BLISS - ARO 27.5" - COLOR ECLIPSE
    # https://www.monark.com.pe/producto/bicicleta-liv-bliss-aro-27-5-color-eclipse/
    # regular price
    # no cart label
    return product_list_first_page[2]

@pytest.fixture
def product_monark_eflash_20_negro(monark_scraper, product_list_last_page):
    # BICICLETA ELÉCTRICA MONARK E-FLASH - ARO 20″ - NEGRO
    # old and special price
    # discount label -25
    # add tocart label
    return product_list_last_page[2]

def test_get_next_page_url(monark_scraper, html_static_content_first_page):
    html_tree = html.fromstring(html_static_content_first_page)
    next_element = monark_scraper.get_next_page_url(html_tree, html_static_content_first_page)
    assert next_element != ""

def test_get_next_page_url_last_page(monark_scraper, html_static_content_last_page):
    html_tree = html.fromstring(html_static_content_last_page)
    next_element = monark_scraper.get_next_page_url(html_tree, html_static_content_last_page)
    assert next_element == ""

def test_get_product_element_list(monark_scraper, html_static_content_first_page):      
    html_tree = html.fromstring(html_static_content_first_page)
    product_list = monark_scraper.get_product_element_list(html_tree)
    assert product_list 
    assert len(product_list) == 15

# ************************
# BICICLETA LIV BLISS - ARO 27.5" - COLOR ECLIPSE
# ************************
def test_get_product_name_liv_bliss_275_eclipse(monark_scraper, product_liv_bliss_275_eclipse):    
    assert monark_scraper.get_product_name(product_liv_bliss_275_eclipse) == 'BICICLETA LIV BLISS - ARO 27.5" - COLOR ECLIPSE'

def test_get_product_link_liv_bliss_275_eclipse(monark_scraper, product_liv_bliss_275_eclipse):    
    assert monark_scraper.get_product_link(product_liv_bliss_275_eclipse) == "https://www.monark.com.pe/producto/bicicleta-liv-bliss-aro-27-5-color-eclipse/"

def test_get_product_image_link_liv_bliss_275_eclipse(monark_scraper, product_liv_bliss_275_eclipse):
    assert monark_scraper.get_product_image_link(product_liv_bliss_275_eclipse) == "https://www.monark.com.pe/wp-content/uploads/MY21-Bliss-27.5_Color-B-Eclipse-min-600x600.jpg"

def test_get_product_old_price_liv_bliss_275_eclipse(monark_scraper, product_liv_bliss_275_eclipse):
    assert monark_scraper.get_product_old_price(product_liv_bliss_275_eclipse) == ""    

def test_get_product_special_price_liv_bliss_275_eclipse(monark_scraper, product_liv_bliss_275_eclipse):
    assert monark_scraper.get_product_special_price(product_liv_bliss_275_eclipse) == ""

def test_get_product_regular_price_liv_bliss_275_eclipse(monark_scraper, product_liv_bliss_275_eclipse):
    assert monark_scraper.get_product_regular_price(product_liv_bliss_275_eclipse) == "2,364.00"

def test_get_product_status_label_liv_bliss_275_eclipse(monark_scraper, product_liv_bliss_275_eclipse):
    assert monark_scraper.get_product_status_label(product_liv_bliss_275_eclipse) == ""

def test_get_product_discount_label_liv_bliss_275_eclipse(monark_scraper, product_liv_bliss_275_eclipse):
    assert monark_scraper.get_product_discount_label(product_liv_bliss_275_eclipse) == ""

def test_get_product_add_to_cart_label_liv_bliss_275_eclipse(monark_scraper, product_liv_bliss_275_eclipse):
    assert monark_scraper.get_product_add_to_cart_label(product_liv_bliss_275_eclipse) == ""

# ************************
# BICICLETA ELÉCTRICA MONARK E-FLASH - ARO 20″ - NEGRO
# ************************
def test_get_product_name_monark_eflash_20_negro(monark_scraper, product_monark_eflash_20_negro):    
    assert monark_scraper.get_product_name(product_monark_eflash_20_negro) == 'BICICLETA ELÉCTRICA MONARK E-FLASH - ARO 20″ - NEGRO'

def test_get_product_old_price_monark_eflash_20_negro(monark_scraper, product_monark_eflash_20_negro):
    assert monark_scraper.get_product_old_price(product_monark_eflash_20_negro) == "4,999.00"

def test_get_product_special_price_monark_eflash_20_negro(monark_scraper, product_monark_eflash_20_negro):
    assert monark_scraper.get_product_special_price(product_monark_eflash_20_negro) == "3,999.00"

def test_get_product_regular_price_monark_eflash_20_negro(monark_scraper, product_monark_eflash_20_negro):
    assert monark_scraper.get_product_regular_price(product_monark_eflash_20_negro) == ""

def test_get_product_status_label_monark_eflash_20_negro(monark_scraper, product_monark_eflash_20_negro):
    assert monark_scraper.get_product_status_label(product_monark_eflash_20_negro) == ""

def test_get_product_discount_label_monark_eflash_20_negro(monark_scraper, product_monark_eflash_20_negro):
    assert monark_scraper.get_product_discount_label(product_monark_eflash_20_negro) == "-20%"

def test_get_product_add_to_cart_label_monark_eflash_20_negro(monark_scraper, product_monark_eflash_20_negro):
    assert monark_scraper.get_product_add_to_cart_label(product_monark_eflash_20_negro) == "COMPRAR"

if __name__ == '__main__':    
    #test_get_product_element_list(monark_scraper(monark_scraper_type()), html_static_content_first_page())
    None