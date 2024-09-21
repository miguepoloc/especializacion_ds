class Person:
    def __init__(self, first_name: str, last_name: str, identification: str, age: int, gender: str) -> None:
        self.__first_name      = first_name
        self.__last_name       = last_name
        self.__identification  = identification
        self.__age             = age
        self.__gender          = gender

    def __validate_identification(self) -> bool:
        return len(self.__identification) > 0

    @property
    def identification(self) -> str:
        if self.__validate_identification():
            return self.__identification
        else:
            return "Invalid ID"

    @identification.setter
    def identification(self, new_id: str):
        if len(new_id) == 4:
            self.__identification = new_id
        else:
            print("New identification must have exactly 4 characters.")


class Employee(Person):
    __company     = 'ETA'
    __base_salary = 1000.34

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
        self.__code           = code
        self.__campus         = campus
        self.__over_time      = over_time
        self.__sales_by_month = sales_by_month
        self.__salary         = Employee.__base_salary

    def __calculate_salary(self) -> float:
        self.__salary = self.__salary + (self.__sales_by_month * 0.3) * self.__over_time
        return self.__salary

    def get_salary(self) -> float:
        return self.__calculate_salary()

    @property
    def sales_by_month(self) -> float:
        return self.__sales_by_month

    @sales_by_month.setter
    def sales_by_month(self, value: float) -> None:
        if value >= 0:
            self.__sales_by_month = value
        else:
            print("Sales by month cannot be negative.")

    def __str__(self) -> str:
        return (
            f"Employee: {self._Person__first_name} {self._Person__last_name} - "
            f"ID: {self.identification}, "
            f"Salary: {self.__salary}, "
            f"Company: {Employee.__company}"
        )


def main():
    employee = Employee('1234', 4, 34.5, 'Sede A', 'Juan', 'Perez', '1234', 25, 'M')

    employee.sales_by_month = 45.0

    print(f"Salary calculated: {employee.get_salary()}")
    print(employee)

    employee.identification = '5678'

    print(f"Updated Employee ID: {employee.identification}")

main()
