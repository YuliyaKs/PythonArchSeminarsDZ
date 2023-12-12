from homework5.product_data.product import Product


# Отзывы покупателя
class UserFeedback:

    user_feedbacks = {}

    def __init__(self, user_feedbacks):
        self.user_feedbacks = user_feedbacks

    # Добавляем отзыв на товар (товар: отзыв)
    def add_feedback(self, product: Product, feedback: str):
        self.user_feedbacks[product] = feedback

    # Удаляем отзыв на товар
    def dell_feedback(self, product):
        self.user_feedbacks.pop(product)
