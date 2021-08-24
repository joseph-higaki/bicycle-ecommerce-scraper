import pandas as pd
import fetch
from lxml import html
import time
import datetime
from product import Product
import utils
import os.path
import scraper_type

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

    def scrape(self):
        product_data = [] 
        url = self.scraper_type.base_url         
        batch_timestamp = datetime.datetime.utcfromtimestamp(time.time()).strftime('%Y-%m-%dT%H:%M:%SZ')        
        while url != "":
            batch_info_object = {"batch_timestamp": batch_timestamp,                                
                                "base_url": self.scraper_type.base_url,
                                "site": utils.extract_domain_from_url(url),
                                "url": url}
            tree = html.fromstring(fetch.get_page_content(url, force_bottom_scroll=True))            
            url = self.get_next_page_url(tree, url)
            product_element_list = self.get_product_element_list(tree)
            for product_element in product_element_list:   
                product = self.get_product(product_element) 
                row_object = dict(
                                batch_info_object,
                                **product.get_data_row())
                product_data.append(row_object)             
        return pd.DataFrame(product_data)      
       
def scrape_site(scraper_type):
    scraper = MyScraper(scraper_type)
    df = scraper.scrape()        
    output_file = "output/ecommerce-bicycles.csv"
    include_header = not os.path.isfile(output_file)
    df.to_csv(output_file, mode='a', header = include_header)


def main():
    # scrape_site(scraper_type.ScraperType.oxford("https://www.oxfordstore.pe/bicicletas.html"))
    # scrape_site(scraper_type.ScraperType.monark("https://www.monark.com.pe/categoria-producto/bicicletas/"))
    # scrape_site(scraper_type.ScraperType.specialized("https://www.specializedperu.com/catalog/category/view/s/bicicletas/id/467/"))
    # scrape_site(scraper_type.ScraperType.specialized("https://www.specializedperu.com/preventa.html"))

    scrape_site(scraper_type.ScraperType.wong("https://www.wong.pe/deportes-y-outdoors/bicicletas"))
    
if __name__ == "__main__":
    main()
