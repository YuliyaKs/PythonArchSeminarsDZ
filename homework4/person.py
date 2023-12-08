class Person:
    def __init__(self, id: int, fio: str, card_number: int, login: str, hash_pass: int):
        self.id = id
        self.fio = fio
        self.card_number = card_number
        self.login = login
        self.hash_pass = hash_pass

    def get_id(self):
        return self.id

    def get_fio(self):
        return self.fio

    def get_login(self):
        return self.login

    def set_login(self, login):
        self.login = login

    def get_hash_pass(self):
        return self.hash_pass

    def set_hash_pass(self, hash_pass):
        self.hash_pass = hash_pass
