from homework1.model_elements.angle_point_color.Point_3d import Point_3d

class Poligon (Point_3d):
    points = Point_3d

    def __init__(self, points):
        self.points = list(points)