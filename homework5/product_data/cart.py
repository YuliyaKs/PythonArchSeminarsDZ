from homework5.product_data.product import Product
from homework5.product_data.shop_products import ShopProducts


class Cart:

    cart_products = []

    def __init__(self, shop: ShopProducts, cart_products):
        self.shop = shop
        self.cart_products = cart_products

    def add_cart_product(self, product: Product):
        if product in self.shop.products:
            self.cart_products.append(product)
            self.shop.products[product] = self.shop.products[product] - 1
        else:
            print("Товар", product.name, "закончился")

    def dell_cart_product(self, product):
        if product in self.cart_products:
            self.cart_products.remove(product)
            self.shop.products[product] = self.shop.products[product] + 1
        else:
            print("В корзине нет товара", product.name)
