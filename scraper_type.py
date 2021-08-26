
class ScraperType:
    def __init__(self, name = "", base_url = ""):
        self.name = name
        self.base_url = base_url        
        self.xpath_product_element_list = ""
        self.xpath_next_page_url = ""
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
    def oxford(cls, base_url):
        scraper_type = cls(name = "oxford", base_url = base_url)
        scraper_type.xpath_product_element_list = '//*[contains(@class, "product-content")]'
        scraper_type.xpath_next_page_url = '//*[contains(@class, "next i-next")]/@href'
        scraper_type.xpath_product_name = './/*[contains(@class, "product-name")]/a/text()'
        scraper_type.xpath_product_link = './/*[contains(@class, "product-name")]/a/@href'
        scraper_type.xpath_product_image_link = './/img/@src'
        scraper_type.xpath_product_status_label = './/*[contains(@class, "product-label")]/span/text()'        
        scraper_type.xpath_product_old_price = './/*[contains(@class, "old-price")]/span/text()'
        scraper_type.xpath_product_special_price = './/*[contains(@class, "special-price")]/span/text()'
        scraper_type.xpath_product_regular_price = './/*[contains(@class, "regular-price")]/span/text()'
        scraper_type.xpath_product_discount_label = ''
        scraper_type.xpath_product_add_to_cart_label = './/*[contains(@title, "Añadir al carro")]/@title'
        return scraper_type


    @classmethod
    def monark(cls, base_url):
        scraper_type = cls(name = "monark", base_url = base_url)
        scraper_type.xpath_product_element_list = '//*[contains(@class, "owl-item")]'
        scraper_type.xpath_next_page_url = '//*[contains(@class, "page-numbers current")]/ancestor::li/following-sibling::li[1]/a/@href'
        scraper_type.xpath_product_name = './/*[contains(@class, "titulo")]/h2/text()'
        scraper_type.xpath_product_link = './/*[contains(@class, "btn")]/@href'
        scraper_type.xpath_product_image_link = './/*[contains(@class, "imagen")]//img/@src'

        scraper_type.xpath_product_status_label = ''  
        scraper_type.xpath_product_old_price = './/*[contains(@class, "price-default")]/del/span/text()'
        scraper_type.xpath_product_special_price = './/*[contains(@class, "price-default")]/ins/span/text()'
        scraper_type.xpath_product_regular_price = './/*[contains(@class, "price-default")]/span/text()'
        scraper_type.xpath_product_discount_label = './/*[contains(@class, "sale-perc")]/text()'
        scraper_type.xpath_product_add_to_cart_label = './/*[contains(@class, "comprar")]/text()'
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

    @classmethod
    def wong(cls, base_url):
        scraper_type = cls(name = "wong", base_url = base_url)
        scraper_type.xpath_product_element_list = '//*[contains(@class, "product-item product-item--")]'
        scraper_type.xpath_next_page_url = ''
        scraper_type.xpath_product_name = './/*[@class="product-item__name"]/text()'
        scraper_type.xpath_product_link = './/*[@class="product-item__name"]/@href'
        scraper_type.xpath_product_image_link = './/*[@class="product-item__image-link"]/div/img/@src'
        scraper_type.xpath_product_status_label = './/*[@class="product-prices__label--discount-label"]/text()'          
        scraper_type.xpath_product_old_price = './/*[@class="product-prices__price product-prices__price--former-price"]/*[@class="product-prices__value"]/text()'
        scraper_type.xpath_product_special_price = './/*[@class="product-prices__price product-prices__price--better-price"]/*[@class="product-prices__value product-prices__value--best-price"]/text()'        
        scraper_type.xpath_product_regular_price = './/*[@class="product-prices__price product-prices__price--regular-price"]/*[@class="product-prices__value product-prices__value--best-price"]/text()'
        scraper_type.xpath_product_discount_label = './/*[@class="flag discount-percent"]/text()'
        scraper_type.xpath_product_add_to_cart_label = './/*[@class="product-add-to-cart__text"]/text()'
        return scraper_type
    
    @classmethod
    def juntoz(cls, base_url):
        scraper_type = cls(name = "juntoz", base_url = base_url)
        scraper_type.xpath_product_element_list = '//*[@class = "catalog-products-body__product-wrapper"]'
        scraper_type.xpath_next_page_url = ''
        scraper_type.xpath_product_name = './/*[contains(@class, "catalog-products-body__product-name__title-hover")]/text()'
        scraper_type.xpath_product_link = './/*[contains(@class, "catalog-products-body__product-name__title-hover")]/@href'
        scraper_type.xpath_product_image_link = './/*[@class = "img-responsive catalog-products-body__product-img-big"]/@src'
        
        scraper_type.xpath_product_status_label = 'TBD'
        scraper_type.xpath_product_old_price = './/*[@class = "ng-binding catalog-products-body__product-old-price"]/text()'        
        scraper_type.xpath_product_special_price = './/*[@class = "catalog-products-body__product-special-price ng-binding ng-scope"]/text()'
        
        scraper_type.xpath_product_regular_price = './/*[@class = "ng-binding catalog-products-body__product-special-price"]/text()'
        scraper_type.xpath_product_discount_label = './/*[@class = "catalog-products-body__product-prices__discount ng-binding ng-scope"]/text()'

        scraper_type.xpath_product_add_to_cart_label = ''
        return scraper_type
    
    @classmethod
    def plazavea(cls, base_url):
        scraper_type = cls(name = "plazavea", base_url = base_url)
        scraper_type.xpath_product_element_list = '//*[contains(@class, "Showcase Showcase")]'
        scraper_type.xpath_next_page_url = ''
        scraper_type.xpath_product_name = './/*[@class = "Showcase__details__text"]/a/text()'
        
        #TBD
        scraper_type.xpath_product_link = './/*[contains(@class, "catalog-products-body__product-name__title-hover")]/@href'
        scraper_type.xpath_product_image_link = './/*[@class = "img-responsive catalog-products-body__product-img-big"]/@src'        
        scraper_type.xpath_product_status_label = 'TBD'
        scraper_type.xpath_product_old_price = './/*[@class = "ng-binding catalog-products-body__product-old-price"]/text()'        
        scraper_type.xpath_product_special_price = './/*[@class = "catalog-products-body__product-special-price ng-binding ng-scope"]/text()'
        
        scraper_type.xpath_product_regular_price = './/*[@class = "ng-binding catalog-products-body__product-special-price"]/text()'
        scraper_type.xpath_product_discount_label = './/*[@class = "catalog-products-body__product-prices__discount ng-binding ng-scope"]/text()'

        scraper_type.xpath_product_add_to_cart_label = ''
        return scraper_type