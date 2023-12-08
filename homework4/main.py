from datetime import date

from homework4.bus_route import BusRoute
from homework4.person import Person
from homework4.ticket import Ticket
from homework4.tickets_buying import TicketsBuying

person = Person(1, 'Иванов Иван Иванович', 1234567890123456, "ivan2000", 9876543210)

ticket = Ticket(2000, date.today(), 10, 20, True, 5, 15)

bus_route = BusRoute(100, "Москва-Воронеж", 30, [])

ticket_buying1 = TicketsBuying(person, ticket, bus_route, True)
ticket_buying2 = TicketsBuying(person, ticket, bus_route, False)

ticket_buying1.print_tickets_buying()
ticket_buying2.print_tickets_buying()
