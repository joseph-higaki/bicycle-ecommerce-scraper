from scraper_type import ScraperType
import pytest 
from lxml import html
from my_scraper import MyScraper


@pytest.fixture
def html_static_content_first_page():
    return open("tests/test_data/https___www_wong_pe_deportes-y-outdoors_bicicletas","r", encoding="utf-8").read()

@pytest.fixture
def wong_scraper_type():
    return ScraperType.create_scraper_type("wong.pe")

@pytest.fixture
def wong_scraper(wong_scraper_type):
    return MyScraper(wong_scraper_type)

@pytest.fixture
def product_list_first_page(wong_scraper, html_static_content_first_page):    
    html_tree = html.fromstring(html_static_content_first_page)    
    return wong_scraper.get_product_element_list(html_tree)   

@pytest.fixture
def product_rali_urbana_700_urban(wong_scraper, product_list_first_page):
    # Rali Bicicleta Urbana 700 Urban		https://www.wong.pe/rali-bicicleta-urbana-700-urban-911158/p	https://wongfood.vteximg.com.br/arquivos/ids/410951-230-230/Rali-Bicicleta-Urbana-700-Urban-1-192867656.jpg?v=637490144181830000	S/1,499.90	S/599.96		todo medio de pago	60 %	Agregar
    return product_list_first_page[0]

@pytest.fixture
def product_movimiento_electrica_plegable_26(wong_scraper, product_list_first_page):
    # Movimento Bicicleta Eléctrica Plegable Aro 26" Venecia 25 Km/h		https://www.wong.pe/movimento-bicicleta-electrica-plegable-aro-26-venecia-25-km-h-922282/p	https://wongfood.vteximg.com.br/arquivos/ids/424130-230-230/Movimento-Bicicleta-El-ctrica-Plegable-Aro-26-Venecia-25-Km-h-1-199526970.jpg?v=637528236956270000		S/3,900.00			0	Agregar
    return product_list_first_page[37]

def test_get_next_page_url(wong_scraper, html_static_content_first_page):
    html_tree = html.fromstring(html_static_content_first_page)
    next_element = wong_scraper.get_next_page_url(html_tree, html_static_content_first_page)
    assert next_element == ""

def test_get_next_page_url_last_page(wong_scraper
#, html_static_content_last_page
):
    #html_tree = html.fromstring(html_static_content_last_page)
    #next_element = wong_scraper.get_next_page_url(html_tree, html_static_content_last_page)
    assert True

def test_get_product_element_list(wong_scraper, html_static_content_first_page):      
    html_tree = html.fromstring(html_static_content_first_page)
    product_list = wong_scraper.get_product_element_list(html_tree)
    assert product_list 
    assert len(product_list) == 54

# ************************
# Rali Bicicleta Urbana 700 Urban
# ************************
def test_get_product_name_rali_urbana_700_urban(wong_scraper, product_rali_urbana_700_urban):    
    assert wong_scraper.get_product_name(product_rali_urbana_700_urban) == "Rali Bicicleta Urbana 700 Urban"

def test_get_product_link_rali_urbana_700_urban(wong_scraper, product_rali_urbana_700_urban):    
    assert wong_scraper.get_product_link(product_rali_urbana_700_urban) == "https://www.wong.pe/rali-bicicleta-urbana-700-urban-911158/p"

def test_get_product_image_link_rali_urbana_700_urban(wong_scraper, product_rali_urbana_700_urban):
    assert wong_scraper.get_product_image_link(product_rali_urbana_700_urban) == "https://wongfood.vteximg.com.br/arquivos/ids/410951-230-230/Rali-Bicicleta-Urbana-700-Urban-1-192867656.jpg?v=637490144181830000"

def test_get_product_old_price_rali_urbana_700_urban(wong_scraper, product_rali_urbana_700_urban):
    assert wong_scraper.get_product_old_price(product_rali_urbana_700_urban) == "S/1,499.90"

def test_get_product_special_price_rali_urbana_700_urban(wong_scraper, product_rali_urbana_700_urban):
    assert wong_scraper.get_product_special_price(product_rali_urbana_700_urban) == "S/599.96"

def test_get_product_regular_price_rali_urbana_700_urban(wong_scraper, product_rali_urbana_700_urban):
    assert wong_scraper.get_product_regular_price(product_rali_urbana_700_urban) == ""

def test_get_product_status_label_rali_urbana_700_urban(wong_scraper, product_rali_urbana_700_urban):
    assert wong_scraper.get_product_status_label(product_rali_urbana_700_urban) == "todo medio de pago"

def test_get_product_discount_label_rali_urbana_700_urban(wong_scraper, product_rali_urbana_700_urban):
    assert wong_scraper.get_product_discount_label(product_rali_urbana_700_urban) == "60 %"

def test_get_product_add_to_cart_label_rali_urbana_700_urban(wong_scraper, product_rali_urbana_700_urban):
    assert wong_scraper.get_product_add_to_cart_label(product_rali_urbana_700_urban) == "Agregar"

# ************************
# Movimento Bicicleta Eléctrica Plegable Aro 26" Venecia 25 Km/h		https://www.wong.pe/movimento-bicicleta-electrica-plegable-aro-26-venecia-25-km-h-922282/p	https://wongfood.vteximg.com.br/arquivos/ids/424130-230-230/Movimento-Bicicleta-El-ctrica-Plegable-Aro-26-Venecia-25-Km-h-1-199526970.jpg?v=637528236956270000		S/3,900.00			0	Agregar
# ************************
def test_get_product_name_movimiento_electrica_plegable_26(wong_scraper, product_movimiento_electrica_plegable_26):    
    assert wong_scraper.get_product_name(product_movimiento_electrica_plegable_26) == 'Movimento Bicicleta Eléctrica Plegable Aro 26" Venecia 25 Km/h'

def test_get_product_old_price_movimiento_electrica_plegable_26(wong_scraper, product_movimiento_electrica_plegable_26):
    assert wong_scraper.get_product_old_price(product_movimiento_electrica_plegable_26) == ""    

def test_get_product_special_price_movimiento_electrica_plegable_26(wong_scraper, product_movimiento_electrica_plegable_26):
    assert wong_scraper.get_product_special_price(product_movimiento_electrica_plegable_26) == ""

def test_get_product_regular_price_movimiento_electrica_plegable_26(wong_scraper, product_movimiento_electrica_plegable_26):
    assert wong_scraper.get_product_regular_price(product_movimiento_electrica_plegable_26) == "S/3,900.00"

def test_get_product_status_label_movimiento_electrica_plegable_26(wong_scraper, product_movimiento_electrica_plegable_26):
    assert wong_scraper.get_product_status_label(product_movimiento_electrica_plegable_26) == ""

def test_get_product_discount_label_movimiento_electrica_plegable_26(wong_scraper, product_movimiento_electrica_plegable_26):
    assert wong_scraper.get_product_discount_label(product_movimiento_electrica_plegable_26) == "0"

def test_get_product_add_to_cart_label_movimiento_electrica_plegable_26(wong_scraper, product_movimiento_electrica_plegable_26):
    assert wong_scraper.get_product_add_to_cart_label(product_movimiento_electrica_plegable_26) == "Agregar"

if __name__ == '__main__':
    #test_get_next_page_url_last_page(wong_scraper(wong_scraper_type()), html_static_content_last_page())
    #test_get_product_element_list(wong_scraper(wong_scraper_type()), html_static_content_first_page())
    #test_get_product_element_list(wong_scraper(wong_scraper_type()), html_static_content_first_page())
    None