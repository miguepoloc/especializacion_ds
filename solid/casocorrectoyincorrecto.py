class Room:
    def __init__(self, number, capacity, price_per_night):
        self.number = number
        self.capacity = capacity
        self.price_per_night = price_per_night
        self.is_booked = False

class Hotel:
    def __init__(self, name, rooms):
        self.name = name
        self.rooms = rooms

    def find_available_room(self, capacity):
        for room in self.rooms:
            if not room.is_booked and room.capacity >= capacity:
                return room
        return None

class Reservation:
    def __init__(self, guest_name, room, check_in_date, check_out_date):
        self.guest_name = guest_name
        self.room = room
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date

    def calculate_total_cost(self):
        total_days = (self.check_out_date - self.check_in_date).days
        return total_days * self.room.price_per_night

# Caso Correcto
room1 = Room(number=101, capacity=2, price_per_night=100)
room2 = Room(number=102, capacity=3, price_per_night=120)
hotel = Hotel(name="Example Hotel", rooms=[room1, room2])

check_in_date = datetime.datetime(2024, 4, 28)
check_out_date = datetime.datetime(2024, 4, 30)
available_room = hotel.find_available_room(capacity=2)
if available_room:
    reservation = Reservation(guest_name="John Doe", room=available_room, check_in_date=check_in_date, check_out_date=check_out_date)
    available_room.is_booked = True
    print("Reservation for {} in room {} confirmed. Total cost: ${}".format(reservation.guest_name, reservation.room.number, reservation.calculate_total_cost()))
else:
    print("No available rooms for the requested dates.")

# Caso Incorrecto
check_in_date = datetime.datetime(2024, 4, 25)
check_out_date = datetime.datetime(2024, 4, 27)
available_room = hotel.find_available_room(capacity=4)
if available_room:
    reservation = Reservation(guest_name="Jane Smith", room=available_room, check_in_date=check_in_date, check_out_date=check_out_date)
    available_room.is_booked = True
    print("Reservation for {} in room {} confirmed. Total cost: ${}".format(reservation.guest_name, reservation.room.number, reservation.calculate_total_cost()))
else:
    print("No available rooms for the requested dates.")
