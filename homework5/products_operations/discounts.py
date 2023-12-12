from homework5.product_data.product import Product


class Discounts:

    discounts = {}

    def __int__(self, discounts):
        self.discounts = discounts

    def add_discount(self, product: Product, discount: int):
        self.discounts[product] = discount

    def dell_product(self, product):
        self.discounts.pop(product)

        