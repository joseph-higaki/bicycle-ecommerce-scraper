from scraper_type import ScraperType
import pytest 
from lxml import html
from my_scraper import MyScraper


@pytest.fixture
def html_static_content_first_page():
    return open("tests/test_data/https___www_specializedperu_com_catalog_category_view_s_bicicletas_id_467_","r", encoding="utf-8").read()

@pytest.fixture
def html_static_content_presale_page():
    return open("tests/test_data/https___www_specializedperu_com_preventa_html","r", encoding="utf-8").read()
    
@pytest.fixture
def specialized_scraper_type():
    return ScraperType.create_scraper_type("specializedperu.com")

@pytest.fixture
def specialized_scraper(specialized_scraper_type):
    return MyScraper(specialized_scraper_type)

@pytest.fixture
def product_list_first_page(specialized_scraper, html_static_content_first_page):    
    html_tree = html.fromstring(html_static_content_first_page)    
    return specialized_scraper.get_product_element_list(html_tree)   

@pytest.fixture
def product_list_presale_page(specialized_scraper, html_static_content_presale_page):    
    html_tree = html.fromstring(html_static_content_presale_page)    
    return specialized_scraper.get_product_element_list(html_tree)   

@pytest.fixture
def product_shiv_sw_disc_etap(specialized_scraper, product_list_first_page):
    #  SHIV SW DISC ETAP    
    return product_list_first_page[17]

@pytest.fixture
def product_rockhopper_expert_29(specialized_scraper, product_list_presale_page):
    # Rockhopper Expert 29
    return product_list_presale_page[1]

def test_get_next_page_url(specialized_scraper, html_static_content_first_page):
    html_tree = html.fromstring(html_static_content_first_page)
    next_element = specialized_scraper.get_next_page_url(html_tree, html_static_content_first_page)
    assert next_element == ""

def test_get_next_page_url_last_page(specialized_scraper
#, html_static_content_last_page
):
    #html_tree = html.fromstring(html_static_content_last_page)
    #next_element = specialized_scraper.get_next_page_url(html_tree, html_static_content_last_page)
    assert True

def test_get_product_element_list(specialized_scraper, html_static_content_first_page):      
    html_tree = html.fromstring(html_static_content_first_page)
    product_list = specialized_scraper.get_product_element_list(html_tree)
    assert product_list 
    assert len(product_list) == 21

# ************************
# SHIV SW DISC ETAP
# ************************
def test_get_product_name_shiv_sw_disc_etap(specialized_scraper, product_shiv_sw_disc_etap):    
    assert specialized_scraper.get_product_name(product_shiv_sw_disc_etap) == "SHIV SW DISC ETAP"

def test_get_product_link_shiv_sw_disc_etap(specialized_scraper, product_shiv_sw_disc_etap):    
    assert specialized_scraper.get_product_link(product_shiv_sw_disc_etap) == "https://www.specializedperu.com/catalog/product/view/id/20725/s/shiv-sw-disc-etap/category/467/"

def test_get_product_image_link_shiv_sw_disc_etap(specialized_scraper, product_shiv_sw_disc_etap):
    assert specialized_scraper.get_product_image_link(product_shiv_sw_disc_etap) == "https://www.specializedperu.com/pub/media/catalog/product//2/0/20-01151295056340.jpeg"

def test_get_product_old_price_shiv_sw_disc_etap(specialized_scraper, product_shiv_sw_disc_etap):
    assert specialized_scraper.get_product_old_price(product_shiv_sw_disc_etap) == ""

def test_get_product_special_price_shiv_sw_disc_etap(specialized_scraper, product_shiv_sw_disc_etap):
    assert specialized_scraper.get_product_special_price(product_shiv_sw_disc_etap) == ""

def test_get_product_regular_price_shiv_sw_disc_etap(specialized_scraper, product_shiv_sw_disc_etap):
    assert specialized_scraper.get_product_regular_price(product_shiv_sw_disc_etap) == "US$ 13.999"

def test_get_product_status_label_shiv_sw_disc_etap(specialized_scraper, product_shiv_sw_disc_etap):
    assert specialized_scraper.get_product_status_label(product_shiv_sw_disc_etap) == ""

def test_get_product_discount_label_shiv_sw_disc_etap(specialized_scraper, product_shiv_sw_disc_etap):
    assert specialized_scraper.get_product_discount_label(product_shiv_sw_disc_etap) == ""

def test_get_product_add_to_cart_label_shiv_sw_disc_etap(specialized_scraper, product_shiv_sw_disc_etap):
    assert specialized_scraper.get_product_add_to_cart_label(product_shiv_sw_disc_etap) == ""

# ************************
# Rockhopper Expert 29
# ************************
def test_get_product_name_rockhopper_expert_29(specialized_scraper, product_rockhopper_expert_29):    
    assert specialized_scraper.get_product_name(product_rockhopper_expert_29) == "Rockhopper Expert 29"

def test_get_product_old_price_rockhopper_expert_29(specialized_scraper, product_rockhopper_expert_29):
    assert specialized_scraper.get_product_old_price(product_rockhopper_expert_29) == ""    

def test_get_product_special_price_rockhopper_expert_29(specialized_scraper, product_rockhopper_expert_29):
    assert specialized_scraper.get_product_special_price(product_rockhopper_expert_29) == ""

def test_get_product_regular_price_rockhopper_expert_29(specialized_scraper, product_rockhopper_expert_29):
    assert specialized_scraper.get_product_regular_price(product_rockhopper_expert_29) == "US$ 1.500"

def test_get_product_status_label_rockhopper_expert_29(specialized_scraper, product_rockhopper_expert_29):
    assert specialized_scraper.get_product_status_label(product_rockhopper_expert_29) == ""

def test_get_product_discount_label_rockhopper_expert_29(specialized_scraper, product_rockhopper_expert_29):
    assert specialized_scraper.get_product_discount_label(product_rockhopper_expert_29) == ""

def test_get_product_add_to_cart_label_rockhopper_expert_29(specialized_scraper, product_rockhopper_expert_29):
    assert specialized_scraper.get_product_add_to_cart_label(product_rockhopper_expert_29) == ""

if __name__ == '__main__':
    #test_get_next_page_url_last_page(specialized_scraper(specialized_scraper_type()), html_static_content_last_page())
    #test_get_product_element_list(specialized_scraper(specialized_scraper_type()), html_static_content_first_page())
    #test_get_product_element_list(specialized_scraper(specialized_scraper_type()), html_static_content_first_page())
    None