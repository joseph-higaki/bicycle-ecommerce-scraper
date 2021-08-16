
class ScraperType:
    def __init__(self, name = "", base_url = ""):
        self.name = name
        self.base_url = base_url        
        self.xpath_product_element_list = ""
        self.xpath_next_page_url = ""
        self.xpath_product_name = ""
        self.xpath_product_link = ""
        self.xpath_product_image_link = ""
        self.xpath_product_label = ""        
        self.xpath_product_old_price = ""
        self.xpath_product_special_price = ""
        self.xpath_product_regular_price = ""
        
    @classmethod
    def oxford(cls, base_url):
        scraper_type = cls(name = "oxford", base_url = base_url)
        scraper_type.xpath_product_element_list = '//*[contains(@class, "product-content")]'
        scraper_type.xpath_next_page_url = '//*[contains(@class, "next i-next")]/@href'
        scraper_type.xpath_product_name = './/*[contains(@class, "product-name")]/a/text()'
        scraper_type.xpath_product_link = './/*[contains(@class, "product-name")]/a/@href'
        scraper_type.xpath_product_image_link = './/img/@src'
        scraper_type.xpath_product_label = './/*[contains(@class, "product-label")]/span/text()'        
        scraper_type.xpath_product_old_price = './/*[contains(@class, "old-price")]/span/text()'
        scraper_type.xpath_product_special_price = './/*[contains(@class, "special-price")]/span/text()'
        scraper_type.xpath_product_regular_price = './/*[contains(@class, "regular-price")]/span/text()'
        return scraper_type


    # @classmethod
    # def monark(cls, base_url):
    #     scraper_type = cls(name = "monark", base_url = base_url)
    #     scraper_type.xpath_product_element_list = '//*[contains(@class, "owl-item")]'
    #     scraper_type.xpath_next_page_url = '//*[contains(@class, "next i-next")]/@href'
    #     scraper_type.xpath_product_name = './/*[contains(@class, "product-name")]/a/text()'
    #     scraper_type.xpath_product_link = './/*[contains(@class, "product-name")]/a/@href'
    #     scraper_type.xpath_product_image_link = './/img/@src'
    #     scraper_type.xpath_product_label = './/*[contains(@class, "product-label")]/span/text()'        
    #     scraper_type.xpath_product_old_price = './/*[contains(@class, "old-price")]/span/text()'
    #     scraper_type.xpath_product_special_price = './/*[contains(@class, "special-price")]/span/text()'
    #     scraper_type.xpath_product_regular_price = './/*[contains(@class, "regular-price")]/span/text()'
    #     return scraper_type



