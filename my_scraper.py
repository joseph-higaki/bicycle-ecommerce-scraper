import pandas as pd
import fetch
from lxml import html
import time
import datetime
from product import Product
import utils
import os.path
import scraper_type
import config

class MyScraper:
    def __init__(self, scraper_type):
        self.scraper_type = scraper_type

    # html tree 
    @staticmethod
    def _get_element_list(tree, xpath_expression):
        return tree.xpath(xpath_expression)

    @staticmethod
    def _get_first_string_element(tree, xpath_expression):
        return_value = ""
        if xpath_expression != "":
            list = tree.xpath(xpath_expression)
            return_value = list[0].strip() if len(list) > 0 else ""
        return return_value

    # tree: lxml.etree._Element
    def get_next_page_url(self, tree, current_url):
        return utils.ensure_absolute_url(current_url, MyScraper._get_first_string_element(tree, self.scraper_type.xpath_next_page_url))
            
    def move_to_next_page_content(self, driver):
        '''
        Used in DOM_ACTION next page type
        It executes the event on the element that loads the next set of items
        '''
        next_object = None
        try:
            next_object = driver.find_element_by_xpath(self.scraper_type.xpath_next_page_object)
        except:
            pass
        if next_object is not None:
            next_object.click() 
        time.sleep(2)
        return False

    # tree: lxml.html.HtmlElement
    def get_product_element_list(self, tree):
        return tree.xpath(self.scraper_type.xpath_product_element_list)  
        
    def get_product_name(self, element):
        return MyScraper._get_first_string_element(element, self.scraper_type.xpath_product_name)      
        
    def get_product_link(self, element):
        return MyScraper._get_first_string_element(element, self.scraper_type.xpath_product_link)          

    def get_product_image_link(self, element):
        return MyScraper._get_first_string_element(element, self.scraper_type.xpath_product_image_link)          

    def get_product_status_label(self, element):
        return MyScraper._get_first_string_element(element, self.scraper_type.xpath_product_status_label)
    
    def get_product_discount_label(self, element):
        return MyScraper._get_first_string_element(element, self.scraper_type.xpath_product_discount_label)
    
    def get_product_add_to_cart_label(self, element):
        return MyScraper._get_first_string_element(element, self.scraper_type.xpath_product_add_to_cart_label)

    def get_product_old_price(self, element):
        return MyScraper._get_first_string_element(element, self.scraper_type.xpath_product_old_price)        

    def get_product_special_price(self, element):
        return MyScraper._get_first_string_element(element, self.scraper_type.xpath_product_special_price)        

    def get_product_regular_price(self, element):
        '''
        '''        
        return MyScraper._get_first_string_element(element, self.scraper_type.xpath_product_regular_price)        

    #element: tag.element
    def get_product(self, element):           
        product = Product()
        product.name = self.get_product_name(element)
        product.link = self.get_product_link(element)
        product.image_link = self.get_product_image_link(element)
        product.status_label = self.get_product_status_label(element)
        product.old_price = self.get_product_old_price(element)
        product.special_price = self.get_product_special_price(element)
        product.regular_price = self.get_product_regular_price(element)
        product.discount_label = self.get_product_discount_label(element) 
        product.add_to_cart_label = self.get_product_add_to_cart_label(element)      
        return product     

    
    def append_products_from_tree(self, tree, batch_info_object, product_data):
        '''
        Parses a lxml.etree._Element that holds a product list and appends the items into product_data         

            Parameters:
                    tree (lxml.etree._Element): Document holding the product list
                    batch_info_object (dict): Constant values from batch that are repreated on each product item 
                    product_data (dict[]): Array of the dictionary product representation

            Returns:
                    Mutates product_data state
        '''
        product_element_list = self.get_product_element_list(tree)
        for product_element in product_element_list:   
            product = self.get_product(product_element) 
            row_object = dict(
                            batch_info_object,
                            **vars(product))
            product_data.append(row_object)       

    def scrape(self):        
        product_data = []
        for url in self.scraper_type.base_urls:        
            batch_timestamp = datetime.datetime.utcfromtimestamp(time.time()).strftime('%Y-%m-%dT%H:%M:%SZ')   
            batch_info_object = {"batch_timestamp": batch_timestamp,                                
                                    "base_url": url,
                                    "site": utils.extract_domain_from_url(url),
                                    "url": url}

            if (self.scraper_type.load_list_type == scraper_type.LOAD_LIST_TYPE_SCROLL or 
                    self.scraper_type.next_page_type == scraper_type.NEXT_PAGE_TYPE_DOM_ACTION):
                product_data.extend(self.scrape_dynamic_list(url, batch_info_object))
            else:
                product_data.extend(self.scrape_static_list(url, batch_info_object))
        return pd.DataFrame(product_data)      

    def scrape_static_list(self, url, batch_info_object):
        if (self.scraper_type.load_list_type == scraper_type.LOAD_LIST_TYPE_SCROLL or 
                self.scraper_type.next_page_type == scraper_type.NEXT_PAGE_TYPE_DOM_ACTION):
            raise Exception("Dynamic behavior not supported")        
        product_data = []
        while url != "":            
            tree = html.fromstring(fetch.get_page_content(url))
            #override url to reflect actual page
            batch_info_object["url"] = url
            self.append_products_from_tree(tree, batch_info_object, product_data)
            ##TODO: extract next url from xpath or template
            url = self.get_next_page_url(tree, url)        
        return product_data
    
    def scrape_dynamic_list(self, url, batch_info_object):
        '''
        Lorem ipsim

            Parameters:
                    url (string): Constant values from batch that are repreated on each product item 
                    batch_info_object (dict[]): Array of the dictionary product representation

            Returns:
                    Mutates product_data state
        '''
        driver = fetch.get_browser()
        try:
            product_data = []
            html_content = ""
            ## Load initial page
            if self.scraper_type.load_list_type == scraper_type.LOAD_LIST_TYPE_SCROLL:
                #driver.get(url);#fetch.scroll_to_bottom(driver);#html_content = driver.page_source
                html_content = fetch.get_dynamic_page_content_bottom_scroll(url, driver)
            else:
                html_content = fetch.get_page_content(url)

            while html_content != "":                
                tree = html.fromstring(html_content)
                #override url to reflect actual page
                batch_info_object["url"] = url
                # parse products into product_data                
                self.append_products_from_tree(tree, batch_info_object, product_data)

                # Load next page content
                # that may or may not be through a DOM event over a dynamically loading page
                html_content = ""
                if self.scraper_type.next_page_type == scraper_type.NEXT_PAGE_TYPE_DOM_ACTION:
                    if self.move_to_next_page_content(driver):
                        if self.scraper_type.load_list_type == scraper_type.LOAD_LIST_TYPE_SCROLL:
                            fetch.scroll_to_bottom(driver)
                        html_content = driver.page_source
                else:
                    ##TODO: extract next url from xpath or template
                    url = self.get_next_page_url(tree, url)
                    if url != "":
                        if self.scraper_type.load_list_type == scraper_type.LOAD_LIST_TYPE_SCROLL:
                            #driver.get(url);#fetch.scroll_to_bottom(driver);#html_content = driver.page_source
                            html_content = fetch.get_dynamic_page_content_bottom_scroll(url, driver)
                        else:
                            html_content = fetch.get_page_content(url)
        finally:
            driver.close()
        return product_data

       
def scrape_site(scraper_type):
    scraper = MyScraper(scraper_type)
    df = scraper.scrape()        
    output_file = "output/ecommerce-bicycles.csv"
    include_header = not os.path.isfile(output_file)
    df.to_csv(output_file, mode='a', header = include_header, index=True, index_label="batch_site_index")


def main():
    cfg = config.Config() # I need a singleton
    for scraper_type_name in cfg.scraper_types():
        scrape_site(scraper_type.ScraperType.create_scraper_type(scraper_type_name))
    #scrape_site(scraper_type.ScraperType.create_scraper_type("linio.com.pe"))
    #scrape_site(scraper_type.ScraperType.create_scraper_type("juntoz"))
    #scrape_site(scraper_type.ScraperType.oxford("https://www.oxfordstore.pe/bicicletas.html"))
    # scrape_site(scraper_type.ScraperType.monark("https://www.monark.com.pe/categoria-producto/bicicletas/"))
    # scrape_site(scraper_type.ScraperType.specialized("https://www.specializedperu.com/catalog/category/view/s/bicicletas/id/467/"))
    # scrape_site(scraper_type.ScraperType.specialized("https://www.specializedperu.com/preventa.html"))

    #scrape_site(scraper_type.ScraperType.wong("https://www.wong.pe/deportes-y-outdoors/bicicletas"))
    # doesnt work scrape_site(scraper_type.ScraperType.juntoz("https://juntoz.com/categorias/deportes-aventura?categories=1172"))

    #scrape_site(scraper_type.ScraperType.plazavea("https://www.plazavea.com.pe/deportes/bicicletas"))
    
if __name__ == "__main__":
    main()
