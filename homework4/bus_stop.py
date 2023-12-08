class BusStop:
    def __init__(self, id: int, name: str, latitude: float,  longitude: float):
        self.id = id
        self.name = name
        self.latitude = latitude
        self.longitude = longitude

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    # Выводим координаты остановки
    def print_coordinates(self):
        print(self.latitude, self.longitude)

    # Изменяем координаты остановки
    def set_coordinates(self, latitude: float, longitude: float):
        self.latitude = latitude
        self.longitude = longitude

