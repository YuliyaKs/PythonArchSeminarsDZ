from homework1.model_elements.Texture import Texture
from homework1.model_elements.Poligon import Poligon


class Poligonal_model:
    textures = [Texture]
    poligons = [Poligon]

    def __init__(self, textures, poligons):
        self.textures = list(textures)
        self.poligons = list(poligons)
