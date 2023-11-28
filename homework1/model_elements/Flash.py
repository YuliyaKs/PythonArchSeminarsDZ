from homework1.model_elements.angle_point_color.Angle_3d import Angle_3d
from homework1.model_elements.angle_point_color.Point_3d import Point_3d
from homework1.model_elements.angle_point_color.Color import Color


class Flash:

    location = Point_3d
    angle = Angle_3d
    color = Color
    power = float

    def __init__(self, location, angle, color, power):

        self.location = location
        self.angle = angle
        self.color = color
        self.power = power

    def rotate(self, Angle_3d):
        return Angle_3d

    def move(self, Point_3d):
        return Point_3d

