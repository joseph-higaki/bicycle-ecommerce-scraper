#import sys
#sys.path.append('../')

from scraper_type import ScraperType
import pytest 
from lxml import html
from my_scraper import MyScraper


@pytest.fixture
def html_static_content_first_page():
    return open("tests/test_data/https___www_monark_com_pe_categoria-producto_bicicletas_").read()

@pytest.fixture
def html_static_content_last_page():
    return open("tests/test_data/https___www_monark_com_pe_categoria-producto_bicicletas__page_6").read()

@pytest.fixture
def monark_scraper_type():
    return ScraperType.monark("")

@pytest.fixture
def monark_scraper(monark_scraper_type):
    return MyScraper(monark_scraper_type)

@pytest.fixture
def product_list_first_page(monark_scraper, html_static_content_first_page):    
    html_tree = html.fromstring(html_static_content_first_page)    
    return monark_scraper.get_product_element_list(html_tree)   

@pytest.fixture
def product_glt_12_bali_blanco(monark_scraper, product_list_first_page):
    # GLT 12 BALI BLANCO
    # old special price
    # oferta
    return product_list_first_page[0]

@pytest.fixture
def product_glt_12_bali_verde(monark_scraper, product_list_first_page):
    # GLT 12 BALI VERDE
    # regular price
    # proximante
    return product_list_first_page[10]

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
    assert len(product_list) == 12

# ************************
# GLT 12 BALI BLANCO
# ************************
def test_get_product_name_glt_12_bali_blanco(monark_scraper, product_glt_12_bali_blanco):    
    assert monark_scraper.get_product_name(product_glt_12_bali_blanco) == "GLT 12 BALI BLANCO"

def test_get_product_link_glt_12_bali_blanco(monark_scraper, product_glt_12_bali_blanco):    
    assert monark_scraper.get_product_link(product_glt_12_bali_blanco) == "https://www.oxfordstore.pe/bicicletas/glt-12-bali-blanco.html"

def test_get_product_image_link_glt_12_bali_blanco(monark_scraper, product_glt_12_bali_blanco):
    assert monark_scraper.get_product_image_link(product_glt_12_bali_blanco) == "https://www.oxfordstore.pe/media/catalog/product/cache/1/thumbnail/533x400/17f82f742ffe127f42dca9de82fb58b1/b/a/bali.jpg"

def test_get_product_old_price_glt_12_bali_blanco(monark_scraper, product_glt_12_bali_blanco):
    assert monark_scraper.get_product_old_price(product_glt_12_bali_blanco) == "S/.429.00"    

def test_get_product_special_price_glt_12_bali_blanco(monark_scraper, product_glt_12_bali_blanco):
    assert monark_scraper.get_product_special_price(product_glt_12_bali_blanco) == "S/.379.00"

def test_get_product_regular_price_glt_12_bali_blanco(monark_scraper, product_glt_12_bali_blanco):
    assert monark_scraper.get_product_regular_price(product_glt_12_bali_blanco) == ""

def test_get_product_status_label_glt_12_bali_blanco(monark_scraper, product_glt_12_bali_blanco):
    assert monark_scraper.get_product_status_label(product_glt_12_bali_blanco) == "Oferta"

def test_get_product_discount_label_glt_12_bali_blanco(monark_scraper, product_glt_12_bali_blanco):
    assert monark_scraper.get_product_discount_label(product_glt_12_bali_blanco) == ""

def test_get_product_add_to_cart_label_glt_12_bali_blanco(monark_scraper, product_glt_12_bali_blanco):
    assert monark_scraper.get_product_add_to_cart_label(product_glt_12_bali_blanco) == "Añadir al carro"

# ************************
# GLT 12 BALI VERDE
# ************************
def test_get_product_name_glt_12_bali_verde(monark_scraper, product_glt_12_bali_verde):    
    assert monark_scraper.get_product_name(product_glt_12_bali_verde) == "GLT 12 BALI VERDE"

def test_get_product_name_glt_12_bali_verde(monark_scraper, product_glt_12_bali_verde):    
    assert monark_scraper.get_product_name(product_glt_12_bali_verde) == "GLT 12 BALI VERDE"

def test_get_product_old_price_glt_12_bali_verde(monark_scraper, product_glt_12_bali_verde):
    assert monark_scraper.get_product_old_price(product_glt_12_bali_verde) == ""    

def test_get_product_special_price_glt_12_bali_verde(monark_scraper, product_glt_12_bali_verde):
    assert monark_scraper.get_product_special_price(product_glt_12_bali_verde) == ""

def test_get_product_regular_price_glt_12_bali_verde(monark_scraper, product_glt_12_bali_verde):
    assert monark_scraper.get_product_regular_price(product_glt_12_bali_verde) == "S/.429.00"

def test_get_product_status_label_glt_12_bali_verde(monark_scraper, product_glt_12_bali_verde):
    assert monark_scraper.get_product_status_label(product_glt_12_bali_verde) == "Próximamente"

def test_get_product_discount_label_glt_1_bali_verde(monark_scraper, product_glt_12_bali_verde):
    assert monark_scraper.get_product_discount_label(product_glt_12_bali_verde) == ""

def test_get_product_add_to_cart_label_glt_12_bali_verde(monark_scraper, product_glt_12_bali_verde):
    assert monark_scraper.get_product_add_to_cart_label(product_glt_12_bali_verde) == ""

if __name__ == '__main__':
    #test_get_next_page_url_last_page(monark_scraper(monark_scraper_type()), html_static_content_last_page())
    test_get_product_element_list(monark_scraper(monark_scraper_type()), html_static_content_first_page())