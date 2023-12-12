from homework5.product_data.product import Product


# Скидки
class Discounts:

    discounts = {}

    def __int__(self, discounts):
        self.discounts = discounts

    # Добавляем скидки в список скидок (товар: скидка)
    def add_discount(self, product: Product, discount_sum: int):
        self.discounts[product] = discount_sum

    # Удаляем скидки из списка скидок
    def dell_product(self, product):
        self.discounts.pop(product)

        