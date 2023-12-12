# Товары для магазина
class Product:
    def __init__(self, id_prod: int, name: str, price: int):
        self.id_prod = id_prod
        self.name = name
        self.price = price

    def get_id_prod(self):
        return self.id_prod

    def set_id_prod(self, id_prod):
        self.id_prod = id_prod

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price


