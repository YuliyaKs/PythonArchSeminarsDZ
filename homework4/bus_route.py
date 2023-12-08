from bus_stop import BusStop


class BusRoute:
    def __init__(self, id: int, remark: str, capacity: int, bus_stops: list[BusStop]):
        self.id = id
        self.remark = remark
        self.capacity = capacity
        self.bus_stops = bus_stops

    def get_remark(self):
        return self.remark

    def set_remark(self, remark):
        self.remark = remark

    def get_capacity(self):
        return self.capacity

    def get_bus_stops(self):
        return self.bus_stops

    # Добавляем новую остановку в маршрут
    def insert_bus_stop(self, index: int, bus_stop_new: BusStop):
        self.bus_stops.insert(self, index, bus_stop_new)

    # Удаляем остановку из маршрута
    def remove_bus_stop(self, bus_stop_old: BusStop):
        self.bus_stops.remove(self, bus_stop_old)

