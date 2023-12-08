from homework4.bus_route import BusRoute
from homework4.person import Person
from homework4.ticket import Ticket


class TicketsBuying:
    def __init__(self, person: Person, ticket: Ticket, bus_route: BusRoute, is_buying: bool):
        self.person = person
        self.ticket = ticket
        self.bus_route = bus_route
        self.is_buying = is_buying

    def set_person(self, person):
        self.person = person

    def set_ticket(self, ticket):
        self.ticket = ticket

    def set_bus_route(self, bus_route):
        self.bus_route = bus_route

    def set_is_buying(self, is_buying):
        self.is_buying = is_buying

    # Выводим результат покупки билета
    def print_tickets_buying(self):
        if self.is_buying:
            print("Билет продан")
        else:
            print("Билет не продан")


