from homework5.product_data.product import Product


# Класс отзывы
class UserFeedback:

    user_feedbacks = {}

    def __init__(self, user_feedbacks):
        self.user_feedbacks = user_feedbacks

    # Добавить отзыв на товар
    def add_feedback(self, product: Product, feedback: str):
        self.user_feedbacks[product] = feedback

    # Удалить отзыв на товар
    def dell_product(self, product):
        self.user_feedbacks.pop(product)
