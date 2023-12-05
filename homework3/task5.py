''' 5) Переписать код в соответствии с Dependency Inversion Principle:
class Car:
def init(self, engine):
self.engine = engine

def start(self):
    self.engine.start()
class PetrolEngine:
def start(self):
pass
Разорвать зависимость классов Car и PetrolEngine. У машины же может быть DieselEngine.
'''

class Car:
    def __init__(self, engine):
        self.engine = engine

    def start(self):
        self.engine.start()


class Engine:
    def start(self):
        pass


class PetrolEngine(Engine):
    def start(self):
        pass


class DieselEngine(Engine):
    def start(self):
        pass
