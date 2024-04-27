#In this case we not use 'Single responsability properties'

class car:
  def __init__(self, start: bool, oilLevel: float) -> None:
    self.start = start
    self.oilLevel = oilLevel

  def TurnOn(self) -> bool:
    if not self.start:
      return self.start
    else:
      return "Is turn On!" if self.oilLevel > 0 and self.start else "Is not turn On"

carro1 = car(True, 10)
print(carro1.TurnOn())
carro1 = car(True, 0)
print(carro1.TurnOn())


#In this case we use 'Single responsibility properties'

class car:
  def __init__(self, start: bool, oilLevel: float) -> None:
    self.start = start
    self.oilLevel = oilLevel

  def TurnOn(self) -> bool:
    return "Is turn On!" if self.start and self.haveGasoline() else "Is not turn On"

  def haveGasoline(self) -> bool:
    return self.oilLevel > 0

carro1 = car(True, 10)
print(carro1.TurnOn())
carro1 = car(True, 0)
print(carro1.TurnOn())