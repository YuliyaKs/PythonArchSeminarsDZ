from homework5.products_operations.cart import Cart


# Оплата товаров в корзине
class ProductsPayment:

    def __init__(self, cart: Cart, client_card: float, shop_wallet: float):
        self.cart = cart
        self.client_card = client_card
        self.shop_wallet = shop_wallet

    # Подсчет общей суммы всех товаров в корзине
    @staticmethod
    def get_total_sum(cart: Cart):
        total_sum = 0
        for product in cart.cart_products:
            total_sum += product.price
        return total_sum

    # Оплата общей суммы
    def products_payment(self, total_sum):
        if self.client_card >= total_sum:
            self.client_card = self.client_card - total_sum  # списание денежных средств со счета клиента
            self.shop_wallet = self.shop_wallet + total_sum  # поступление денежных средств на счет магазина
            self.cart.cart_products = []  # обнуление товаров в корзине у покупателя после оплаты
            print("Товары оплачены,", total_sum, "рублей")

