#Abstrayendo las características de un monitor importantes para realizar una compra

class Monitor():
  marcas = {
  1:"samsung",
  2:"razer",
  3:"asus"
}
  dimensions = {
    1: 24,
    2: 27,
    3: 32,
    4: 36,
    5: 40
  }

  def __init__(self, precio: float, dimension: float, marca: str, estado: bool):
    self.precio = precio
    self.dimension = dimension
    self.marca = marca.lower()
    self.estado = estado

  def comprar(self):
    pass

#Heredando de la clase padre a 2 clases hijas

class Oficina(Monitor):
  def comprar(self) -> str:
    if not self.marca in self.marcas.values():
      return "No comprar, porque no está la marca requerida"

    if not self.dimension in self.dimensions.values():
      return "No comprar, porque no está el tamaño"

    return f"He comprado un monitor nuevo {self.marca} de {self.dimension} pulgadas a {self.precio} pesos"


class Gamer(Monitor):
  def __init__(self, precio: float, dimension: float, marca: str, estado: bool, frecuencia: int, tecnologia: str) -> None:
    super().__init__(precio=precio, dimension=dimension, marca=marca, estado=estado)
    self.frecuencia = frecuencia
    self.tecnologia = tecnologia.lower()

  def comprar(self) -> str:
    if not (self.estado):
      return "No comprar, porque está usado"

    if not (self.frecuencia > 120):
      return "No comprar, porque no tiene la suficiente tasa de refresco"

    if not (self.tecnologia == "gsync" or self.tecnologia == "freesync"):
      return "No comprar, porque tiene G-Sync ni FreeSync"

    if not self.dimension in self.dimensions.values():
      return "No comprar, porque no está el tamaño"

    return [f"He comprado un monitor nuevo {self.marca} de {self.dimension} pulgadas con tasa de refresco de {self.frecuencia} con {self.tecnologia} a {self.precio} pesos"]

miNewMonitorGamer = Gamer(250, 27, "asus", True, 121, "Gsync")
print(miNewMonitorGamer.comprar())

miNewMonitorOficina = Oficina(250,27,"asuS", False)
print(miNewMonitorOficina.comprar())