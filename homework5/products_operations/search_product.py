from homework5.product_data.shop_products import ShopProducts


class SearchProduct:

    found_products = []

    def __init__(self, shop: ShopProducts, found_products):
        self.shop = shop
        self.found_products = found_products

    def search_products(self, search_query: str):
        for product in self.shop.products:
            if search_query in product.get_name():
                self.found_products.append(product)

    def get_found_products(self):
        return self.found_products

