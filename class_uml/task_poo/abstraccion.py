#Abstrayendo las características de un monitor importantes para realizar una compra

class Monitor():
  def __init__(self, precio: float, dimension: float, marca: str, estado: bool):
    self.precio = precio
    self.dimension = dimension
    self.marca = marca.lower()
    self.estado = estado

  def comprar(self):
    pass