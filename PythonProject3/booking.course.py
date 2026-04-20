class Flight:
    def __init__(self, flight_number, destination, seats):
        self.flight_number = flight_number
        self.destination = destination
        self.total_seats = seats
        self.booked_seats = 0

    def free_seats(self):
        return self.booked_seats < self.total_seats

    def book_seat(self):
        if self.free_seats():
            self.booked_seats += 1
            return True
        return False

    def __str__(self):
        return f"Рейс {self.flight_number} | Куда: {self.destination} | Мест: {self.booked_seats}/{self.total_seats}"


class BookingSystem:
    def __init__(self):
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def find_flight_by_destination(self, destination):
        return [f for f in self.flights if f.destination.lower() == destination.lower()]

    def book_ticket(self, flight_number, passenger_name):
        for flight in self.flights:
            if flight.flight_number == flight_number:
                if flight.book_seat():
                    print(f"Билет для {passenger_name} успешно оформлен на рейс {flight_number}!")
                    return True
                else:
                    print("К сожалению, все места проданы.")
                    return False
        print("Рейс не найден.")
        return False


system = BookingSystem()
system.add_flight(Flight("KC-101", "Алматы", 2))
system.add_flight(Flight("KC-202", "Стамбул", 100))

destiny = "Алматы"
found = system.find_flight_by_destination(destiny)

if found:
    print(f"Найдены рейсы в {destiny}:")
    for f in found:
        print(f)

    system.book_ticket("KC-101", "Altynay")
    system.book_ticket("KC-101", "Talant")
    system.book_ticket("KC-101", "bala")
else:
    print("Рейсов нет.")