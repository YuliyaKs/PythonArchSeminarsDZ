from homework5.product_data.cart import Cart


class ProductsPayment:

    def __init__(self, cart: Cart, client_cart: float, shop_wallet: float):
        self.cart = cart
        self.client_cart = client_cart
        self.shop_wallet = shop_wallet

    @staticmethod
    def get_total_sum(cart: Cart):
        total_sum = 0
        for product in cart.cart_products:
            total_sum += product.price
        return total_sum

    def products_payment(self, total_sum):
        if self.client_cart >= total_sum:
            self.client_cart = self.client_cart - total_sum
            self.shop_wallet = self.shop_wallet + total_sum
            self.cart.cart_products = []
            print("Товары оплачены,", total_sum, "рублей")

