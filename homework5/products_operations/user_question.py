from homework5.product_data.product import Product

# Вопросы покупателя о товаре
class UserQuestion:

    user_questions = {}
    getting_answers = {}

    def __init__(self, user_questions, getting_answers):
        self.user_questions = user_questions
        self.getting_answers = getting_answers

    # Добавляем вопрос о товаре (товар: вопрос)
    def add_question(self, product: Product, question: str):
        self.user_questions[product] = question

    # Удаляем вопрос о товаре
    def dell_question(self, product):
        self.user_questions.pop(product)

    # Проверяем наличия ответа на вопрос
    def check_answer(self, product):
        if product in self.user_questions:
            if product in self.getting_answers:
                print(self.getting_answers[product])
            else:
                print("Ответа еще нет")
        else:
            print("Вы не задавали вопрос")


