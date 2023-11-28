from homework1.model_elements.Poligonal_model import Poligonal_model
from homework1.model_elements.Flash import Flash

class Scene:
    id: int
    models = [Poligonal_model]
    flashes = [Flash]

    def __init__(self, id, models, flashes):
        self.id = id
        self.models = models
        self.flashes = flashes

    def method1(self, type1):
        return type(type1)

    def method2(self, type2):
        return type(type2)