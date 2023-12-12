from homework5.product_data.product import Product


class ShopProducts:

    products = {}

    def __init__(self, products):
        self.products = products

    # Добавляем товар в магазин (товар: количество)
    def add_product(self, product: Product, quantity: int):
        self.products[product] = quantity

    # Удаляем товар из магазина
    def dell_product(self, product):
        self.products.pop(product)




