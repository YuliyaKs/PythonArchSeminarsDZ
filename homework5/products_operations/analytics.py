from homework5.product_data.cart import Cart
from homework5.product_data.shop_products import ShopProducts


class Analytics:

    # Количество видов товаров в магазине
    @staticmethod
    def products_amount(shop: ShopProducts):
        return len(shop.products)

    # Количество видов товаров в корзине
    @staticmethod
    def cart_products_amount(cart: Cart):
        return len(cart.cart_products)

    # Товар в наибольшем количестве в магазине
    @staticmethod
    def max_quantity(shop: ShopProducts):
        return max(shop.products.values())



