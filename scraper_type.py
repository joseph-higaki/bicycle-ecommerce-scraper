'''
Types of page load for the product list
STATIC: Page loads once in plain html
SROLL: Page needs be scrolled to the bottom to load next batch of items
'''
LOAD_LIST_TYPE_STATIC = "STATIC"
LOAD_LIST_TYPE_SCROLL = "SCROLL"

'''
NEXT_URL_ALINK: A html tag holds the link to the next page
PAGE_URL_TEMPLATE_ITERATOR: URL with a page number placeholder 
DOM_ACTION: Renders next set of items in client side 
'''
NEXT_PAGE_TYPE_NEXT_URL_ALINK = "NEXT_URL_ALINK"
NEXT_PAGE_TYPE_PAGE_URL_TEMPLATE_ITERATOR = "PAGE_URL_TEMPLATE_ITERATOR"
NEXT_PAGE_TYPE_DOM_ACTION = "DOM_ACTION"

import config

class ScraperType:
    def __init__(self, name = ""):
        self.name = name
        self.load_list_type = LOAD_LIST_TYPE_STATIC
        self.next_page_type = NEXT_PAGE_TYPE_NEXT_URL_ALINK
        self.base_urls = []
        self.next_page_url_template_iterator = ""
        self.xpath_product_element_list = ""        
        self.xpath_next_page_url = ""
        self.xpath_next_page_object = ""
        self.xpath_product_name = ""
        self.xpath_product_link = ""
        self.xpath_product_image_link = ""
        self.xpath_product_status_label = ""    
        self.xpath_product_discount_label = ""
        self.xpath_product_old_price = ""
        self.xpath_product_special_price = ""
        self.xpath_product_regular_price = ""
        self.xpath_product_add_to_cart_label = ""       

    @classmethod
    def create_scraper_type(cls, scraper_type_name):
        cfg = config.Config() # I need a singleton
        scraper_type = cls(name = scraper_type_name)

        scraper_type.load_list_type = cfg.get_attribute(scraper_type_name, "load_list_type") 
        scraper_type.next_page_type = cfg.get_attribute(scraper_type_name, "next_page_type") 
        scraper_type.base_urls = cfg.get_attribute(scraper_type_name, "base_urls") 
        scraper_type.next_page_url_template_iterator = cfg.get_attribute(scraper_type_name, "next_page_url_template_iterator") 

        scraper_type.xpath_product_element_list = cfg.get_attribute(scraper_type_name, "xpath_product_element_list")
        scraper_type.xpath_next_page_url = cfg.get_attribute(scraper_type_name, "xpath_next_page_url")
        scraper_type.xpath_product_name = cfg.get_attribute(scraper_type_name, "xpath_product_name")
        scraper_type.xpath_product_link = cfg.get_attribute(scraper_type_name, "xpath_product_link")
        scraper_type.xpath_product_image_link = cfg.get_attribute(scraper_type_name, "xpath_product_image_link")
        scraper_type.xpath_product_status_label = cfg.get_attribute(scraper_type_name, "xpath_product_status_label")
        scraper_type.xpath_product_old_price = cfg.get_attribute(scraper_type_name, "xpath_product_old_price")
        scraper_type.xpath_product_special_price = cfg.get_attribute(scraper_type_name, "xpath_product_special_price")
        scraper_type.xpath_product_regular_price = cfg.get_attribute(scraper_type_name, "xpath_product_regular_price")
        scraper_type.xpath_product_discount_label = cfg.get_attribute(scraper_type_name, "xpath_product_discount_label")
        scraper_type.xpath_product_add_to_cart_label = cfg.get_attribute(scraper_type_name, "xpath_product_add_to_cart_label")
        return scraper_type

        


    @classmethod
    def specialized(cls, base_url):
        scraper_type = cls(name = "specialized", base_url = base_url)
        scraper_type.xpath_product_element_list = '//*[contains(@class, "item product product-item")]'
        
        scraper_type.xpath_next_page_url = ''
        scraper_type.xpath_product_name = './/*[contains(@class, "product name product-item-name text-center")]/a/text()'
        scraper_type.xpath_product_link = './/*[contains(@class, "product name product-item-name text-center")]/a/@href'
        scraper_type.xpath_product_image_link = './/*[contains(@class, "product-image-photo")]/@src'

        scraper_type.xpath_product_status_label = ''  
        scraper_type.xpath_product_old_price = ''
        scraper_type.xpath_product_special_price = ''
        scraper_type.xpath_product_regular_price = './/*[contains(@class, "price-wrapper price-including-tax")]/span/text()'
        scraper_type.xpath_product_discount_label = ''
        scraper_type.xpath_product_add_to_cart_label = ''
        return scraper_type