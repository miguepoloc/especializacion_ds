#In this case we not user interfaces segregation

class Employee:
  def __init__(self, name: str, age: int, ocupation: str) -> None:
    self.name = name
    self.age = age
    self.ocupation = ocupation

  def enterCompany(self) -> str:
    pass

  def driveCompanyCar(self) -> str:
    pass

  def hireEmployees(self) -> str:
    pass

  def terminateEmployees(self) -> str:
    pass

  def buyResources(self) -> str:
    pass


class CEO(Employee):
  def enterCompany(self) -> None:
    return "Successfull"

  def driveCompanyCar(self) -> None:
    return "Drived"

  def hireEmployees(self, newEmployee: str) -> str:
    return f"Haz contratado a : {newEmployee}"

  def terminateEmployees(self, oldEmployee: str) -> str:
    raise f"Haz despedido a : {oldEmployee}"

  def buyResources(self, money: float, resource: str) -> str:
    return f"Haz destinado {money} USD para comprar: {resource}"

#El obrero no debería tener la capacidad para
class Worker(Employee):
  def enterCompany(self) -> str:
    return "Successfull"

  def driveCompanyCar(self) -> str:
    return "Drived"

  def hireEmployees(self) -> str:
    pass

  def terminateEmployees(self) -> str:
    pass

  def buyResources(self) -> str:
    pass

#In this case we not user interfaces segregation
from abc import ABC, abstractmethod

class Employee:
  def __init__(self, name: str, age: int, ocupation: str) -> None:
    self.name = name
    self.age = age
    self.ocupation = ocupation


class Operational(ABC):
  @abstractmethod
  def enterCompany(self) -> str:
    pass

  @abstractmethod
  def driveCompanyCar(self) -> str:
    pass

class Administrative(ABC):
  @abstractmethod
  def hireEmployees(self) -> str:
    pass

  @abstractmethod
  def terminateEmployees(self) -> str:
    pass

  @abstractmethod
  def buyResources(self) -> str:
    pass

class CEO(Employee, Operational, Administrative):
  def enterCompany(self) -> str:
    return "Successfull"

  def driveCompanyCar(self) -> str:
    return "Drived"

  def hireEmployees(self, newEmployee: str) -> str:
    return f"Haz contratado a : {newEmployee}"

  def terminateEmployees(self, oldEmployee: str) -> str:
    raise f"Haz despedido a : {oldEmployee}"

  def buyResources(self, money: float, resource: str) -> str:
    return f"Haz destinado {money} USD para comprar: {resource}"

#El obrero no debería tener la capacidad para realizar acciones administrativas,
#por tanto no hereda esa interfaz
class Worker(Employee, Operational):
  def enterCompany(self) -> str:
    return "Successfull"

  def driveCompanyCar(self) -> str:
    return "Drived"