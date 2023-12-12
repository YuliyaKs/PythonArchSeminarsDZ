from homework5.products_operations.discounts import Discounts
from homework5.products_operations.search_product import SearchProduct


# Отображение нужных товаров пользователю
class ShowFoundProducts:

    # Выводим список товаров по ключевому слову, а также сумму с учетом скидки, если она есть
    @staticmethod
    def show_found_products(search_product: SearchProduct, user_discount: Discounts, search_query: str):
        search_product.search_products(search_query)  # находим товары по ключевому слову
        for product in search_product.get_found_products():
            print(product.get_name(), product.get_price())  # выводим на экран найденные товары
            if product in user_discount.discounts:  # проверяем список скидок
                print("Сумма с учетом скидки:", product.get_price() -
                      product.get_price() * user_discount.discounts[product] / 100)  # стоимость товара с учетом скидки



