from datetime import date


class Ticket:
    def __init__(self, price: float, date_out: date, start_zone: int, finish_zone: int, is_luggage: bool,
                 place: int, road_number: int):
        self.price = price
        self.date_out = date_out
        self.start_zone = start_zone
        self.finish_zone = finish_zone
        self.is_luggage = is_luggage
        self.place = place
        self.road_number = road_number

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def get_date_out(self):
        return self.date_out

    def set_date_out(self, date_out):
        self.date_out = date_out

    def get_start_zone(self):
        return self.start_zone

    def set_start_zone(self, start_zone):
        self.start_zone = start_zone

    def get_finish_zone(self):
        return self.finish_zone

    def set_finish_zone(self, finish_zone):
        self.finish_zone = finish_zone

    def get_place(self):
        return self.place

    def set_place(self, place):
        self.place = place

    def get_road_number(self):
        return self.road_number
