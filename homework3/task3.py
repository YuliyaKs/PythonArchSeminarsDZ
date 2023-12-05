''' 3) Переписать код в соответствии с Interface Segregation Principle:
from abc import ABC, abstractmethod
import math

class Shape(ABC):
@abstractmethod
def area(self):
pass

@abstractmethod
def volume(self):
    pass
class Circle(Shape):
def init(self, radius):
self.radius = radius

def area(self):
    return 2 * math.pi * self.radius

def volume(self):
    raise NotImplementedError("Circle does not have volume")
class Cube(Shape):
def init(self, edge):
self.edge = edge

def area(self):
    return 6 * self.edge * self.edge

def volume(self):
    return self.edge * self.edge * self.edge

Подсказка: круг не объемная фигура и этому классу не нужен метод volume().
'''

from abc import ABC, abstractmethod
import math

# Интерфейс для расчета площади фигуры
class ShapeArea(ABC):
    @abstractmethod
    def area(self):
        pass

# Интерфейс для расчета объема фигуры
class ShapeVolume(ABC):
    @abstractmethod
    def volume(self):
        pass


class Circle(ShapeArea):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 2 * math.pi * self.radius


class Cube(ShapeArea, ShapeVolume):
    def __init__(self, edge):
        self.edge = edge

    def area(self):
        return 6 * self.edge * self.edge

    def volume(self):
        return self.edge * self.edge * self.edge
