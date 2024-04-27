#In this case we not use Open / closed principle

class Employee:
  def __init__(self, name: str, salary: float, typeOfEmployee: str) -> None:
    self.name = name
    self.salary = salary
    self.typeOfEmployee = typeOfEmployee

  def calculateBonus(self) -> float:
    if self.typeOfEmployee == "part-time":
      return self.salary * 0.06
    if self.typeOfEmployee == "full-time":
      return self.salary * 0.1

  def getPayment(self) -> str:
    full_pay = self.salary + self.calculateBonus()
    return f"Su pago es de : {full_pay}"

#In this case we not use Open / closed principle

class Employee:
  def __init__(self, name: str, salary: float, typeOfEmployee: str) -> None:
    self.name = name
    self.salary = salary
    self.typeOfEmployee = typeOfEmployee

  def calculateBonus(self) -> float:
    return 0

class partTimeEmployee(Employee):
  def __init__(self, name: str, salary: float, typeOfEmployee: str) -> None:
    super().__init__(name, salary, typeOfEmployee)

  def calculateBonus(self) -> float:
    return self.salary * 0.6

class fullTimeEmployee(Employee):
  def __init__(self, name: str, salary: float, typeOfEmployee: str) -> None:
    super().__init__(name, salary, typeOfEmployee)

  def calculateBonus(self) -> float:
    return self.salary * 0.1