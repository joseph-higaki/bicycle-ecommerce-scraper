class Product:
    def __init__(self, name = ""):
        self.name = name
        self.id = ""
        self.link = ""
        self.image_link = ""
        self.old_price = ""
        self.special_price = ""
        self.regular_price = ""
        self.status_label = ""
        self.discount_label = ""
        self.add_to_cart_label = ""

    def get_data_row(self):
        return {"product_name": self.name,
                "product_id": self.id,
                "product_link": self.link,
                "product_image_link": self.image_link,
                "product_old_price": self.old_price,
                "product_special_price": self.special_price,
                "product_regular_price": self.regular_price,
                "product_status_label": self.status_label,
                "product_discount_label": self.discount_label,
                "product_add_to_cart_label": self.add_to_cart_label}