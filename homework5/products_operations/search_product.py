from homework5.product_data.shop_products import ShopProducts

# Поиск товаров по ключевому слову
class SearchProduct:

    found_products = []

    def __init__(self, shop: ShopProducts, found_products):
        self.shop = shop
        self.found_products = found_products

    # Находим товары по ключевому слову
    def search_products(self, search_query: str):
        for product in self.shop.products:
            if search_query in product.get_name():
                self.found_products.append(product)  # добавляем товары в список найденных товаров

    # Возвращаем список найденных товаров
    def get_found_products(self):
        return self.found_products

