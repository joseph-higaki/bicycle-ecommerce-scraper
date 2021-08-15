import pandas as pd
import fetch
from lxml import html
import time
import datetime
from product import Product
import utils
import os.path


class MyScraper:
# html tree 
    def _get_element_list(tree, xpath_expression):
        return tree.xpath(xpath_expression)

    def _get_first_string_element(tree, xpath_expression):
        list = tree.xpath(xpath_expression)    
        return list[0].strip() if len(list) > 0 else ""

    # tree: lxml.etree._Element
    def get_next_page_url(tree):
        return MyScraper._get_first_string_element(tree, '//*[contains(@class, "next i-next")]/@href')
            
    # tree: lxml.html.HtmlElement
    def get_product_element_list(tree):
        return tree.xpath('//*[contains(@class, "product-content")]')  
        
    def get_product_name(element):
        return MyScraper._get_first_string_element(element, './/*[contains(@class, "product-name")]/a/text()')      
        

    def get_product_link(element):
        return MyScraper._get_first_string_element(element, './/*[contains(@class, "product-name")]/a/@href')          

    def get_product_image_link(element):
        return MyScraper._get_first_string_element(element, './/img/@src')          

    def get_product_label(element):
        return MyScraper._get_first_string_element(element, './/*[contains(@class, "product-label")]/span/text()')        

    def get_product_old_price(element):
        return MyScraper._get_first_string_element(element, './/*[contains(@class, "old-price")]/span/text()')        

    def get_product_special_price(element):
        return MyScraper._get_first_string_element(element, './/*[contains(@class, "special-price")]/span/text()')        

    def get_product_regular_price(element):
        return MyScraper._get_first_string_element(element, './/*[contains(@class, "regular-price")]/span/text()')        

    #element: tag.element
    def get_product(element):    
        product = Product()
        product.name = MyScraper.get_product_name(element)
        product.link = MyScraper.get_product_link(element)
        product.image_link = MyScraper.get_product_image_link(element)
        product.label = MyScraper.get_product_label(element)
        product.old_price = MyScraper.get_product_old_price(element)
        product.special_price = MyScraper.get_product_special_price(element)
        product.regular_price = MyScraper.get_product_regular_price(element)
        return product     

    def scrape(base_url):
        product_data = [] 
        url = base_url 
        batch_timestamp = datetime.datetime.utcfromtimestamp(time.time()).strftime('%Y-%m-%dT%H:%M:%SZ')        
        while url != "":
            batch_info_object = {"batch_timestamp": batch_timestamp,
                                "base_url": base_url,
                                "site": utils.extract_domain_from_url(url),
                                "url": url}
            tree = html.fromstring(fetch.get_page_content(url))            
            url = MyScraper.get_next_page_url(tree)
            product_element_list = MyScraper.get_product_element_list(tree)
            for product_element in product_element_list:   
                product = MyScraper.get_product(product_element) 
                row_object = dict(
                                batch_info_object,
                                **product.get_data_row())
                product_data.append(row_object)             
        return pd.DataFrame(product_data)      
       
def main():
    df = MyScraper.scrape("https://www.oxfordstore.pe/bicicletas.html")        
    output_file = "output/ecommerce-bicycles.csv"
    include_header = not os.path.isfile(output_file)
    df.to_csv(output_file, mode='a', header = include_header)
if __name__ == "__main__":
    # execute only if run as a script
    main()