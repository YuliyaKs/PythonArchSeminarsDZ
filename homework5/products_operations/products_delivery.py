# Доставка товара
class ProductsDelivery:

    def __init__(self, is_delivered: bool):
        self.is_delivered = is_delivered

    # Оформление доставки товара
    def products_delivery(self):
        self.is_delivered = True
        print("Ожидайте доставку завтра")
