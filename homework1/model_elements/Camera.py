from homework1.model_elements.angle_point_color.Angle_3d import Angle_3d
from homework1.model_elements.angle_point_color.Point_3d import Point_3d


class Camera:
    location = Point_3d
    angle = Angle_3d

    def __init__(self, location, angle):
        self.location = location
        self.angle = angle

    def rotate(self, location):
        pass

    def move(self, angle):
        pass
