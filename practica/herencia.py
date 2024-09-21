class Person:
    def __init__(self, first_name: str, last_name: str, identification: str, age: int, gender: str) -> None:
        self._first_name     = first_name
        self._last_name      = last_name
        self._identification = identification
        self._age            = age
        self._gender         = gender


class Employee(Person):
    _compay = 'ETA'
    _salary = 1000.34

    def __init__(
        self,
        code: str,
        over_time: int,
        sales_by_month: float,
        campus: str,
        first_name: str,
        last_name: str,
        identification: str,
        age: int,
        gender: str
    ) -> None:
        super().__init__(first_name, last_name, identification, age, gender)
        self._code          = code
        self._campus        = campus
        self._over_time     = over_time
        self._sales_by_month = sales_by_month

    def calculate_salary(self) -> float:
        self._salary = self._salary + (self._sales_by_month * 0.3) * self._over_time

    def __str__(self) -> str:
        return (f"Employee: {self._first_name} {self._last_name} - ID: {self._identification}, Salary: {self._salary}, Company: {self._compay}")


def main():
    employee: Employee = Employee('1234', 4.3, 34.5, 'sede A', 'Juan', 'Perez', '1234', 25, 'M')
    employee.calculate_salary()
    print(employee)

main()
