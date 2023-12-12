from homework5.product_data.product import Product


class UserQuestion:

    user_questions = {}
    getting_answers = {}

    def __init__(self, user_questions, getting_answers):
        self.user_questions = user_questions
        self.getting_answers = getting_answers

    # Добавить вопрос о товаре
    def add_question(self, product: Product, question: str):
        self.user_questions[product] = question

    # Удалить вопрос о товаре
    def dell_product(self, product):
        self.user_questions.pop(product)

    # Проверка наличия ответа
    def check_answer(self, product):
        if product in self.user_questions:
            if product in self.getting_answers:
                print(self.getting_answers[product])
            else:
                print("Ответа еще нет")
        else:
            print("Вы не задавали вопрос")


