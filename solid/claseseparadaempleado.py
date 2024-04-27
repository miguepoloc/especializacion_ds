class Employee:
    def __init__(self, name: str, hours_worked: int, hourly_rate: float) -> None:
        self.name: str = name
        self.hours_worked: int = hours_worked
        self.hourly_rate: float = hourly_rate

    def get_name(self) -> str:
        return self.name

    def calculate_pay(self) -> float:
        return self.hours_worked * self.hourly_rate

    def print_pay_stub(self) -> None:
        print("Pay Stub")
        print("Name: ", self.get_name())
        print("Hours Worked: ", self.hours_worked)
        print("Hourly Rate: ", self.hourly_rate)
        print("Gross Pay: ", self.calculate_pay())


class Reservation:
    def __init__(self, guest_name: str, employee1: Employee, employee2: Employee) -> None:
        self.guest_name = guest_name
        self.employee1 = employee1
        self.employee2 = employee2

    def print_reservation_details(self) -> None:
        print("Reservation Details")
        print("Guest Name: ", self.guest_name)
        print("Employee 1:")
        self.employee1.print_pay_stub()
        print("Employee 2:")
        self.employee2.print_pay_stub())



employee1 = Employee("John", 40, 10.0)
employee2 = Employee("Alice", 35, 12.0)


reservation = Reservation("Guest123", employee1, employee2)

# Imprimir los detalles de la reserva
reservation.print_reservation_details()
