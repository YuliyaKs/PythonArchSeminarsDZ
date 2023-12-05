''' 4) Переписать код в соответствии с Liskov Substitution Principle:
class Rectangle:
def init(self):
self.width = 0
self.height = 0

def setWidth(self, width):
    self.width = width

def setHeight(self, height):
    self.height = height

def area(self):
    return self.width * self.height
class Square(Rectangle):
def setWidth(self, width):
self.width = width
self.height = width

def setHeight(self, height):
    self.width = height
    self.height = height
'''

class ShapeRectangles:
    def area(self):
        pass

class Rectangle(ShapeRectangles):
    def __init__(self):
        self.width = 0
        self.height = 0

    def setWidth(self, width):
        self.width = width

    def setHeight(self, height):
        self.height = height

    def area(self):
        return self.width * self.height

class Square(ShapeRectangles):
    def __init__(self):
        self.side = 0

    def setSide(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

