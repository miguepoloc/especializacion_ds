#In this case we not use 'Single responsability properties'

class car:
  def __init__(self, start: bool, oilLevel: float) -> None:
    self.start = start
    self.oilLevel = oilLevel

  def TurnOn(self) -> bool:
    if not self.start:
      return self.start
    else:
      return self.oilLevel > 0 and self.start

#In this case we use 'Single responsibility properties'

class car:
  def __init__(self, start: bool, oilLevel: float) -> None:
    self.start = start
    self.oilLevel = oilLevel

  def TurnOn(self) -> bool:
    return self.start and self.haveGasoline()

  def haveGasoline(self) -> bool:
    return self.oilLevel > 0
