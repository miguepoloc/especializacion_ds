# %% [markdown]
# Caso Practico : Conseccionario de Carros

# %%
from enum import Enum

# %%
class StateCarConseccionario(Enum):
    CREADO = 0
    VENDIDO = 1
    ALQUILADO = 2
    DEVUELTO  = 3


# %%
class NumeroDePuertas (Enum):

    DOS_PUERTAS = 10
    CUATRO_PUERTAS = 20


# %%
class NumeroDePuestos (Enum):
    DOS_PUESTOS = 10
    CUATRO_PUESTOS = 20
    SEIS_PUESTOS = 25

# %%
class CarConcesionario :
    def __init__(self, precio_base: float,
                  caballos_fuerza: int,
                  estado :StateCarConseccionario,
                  numero_de_puestos : NumeroDePuestos,
                  numero_de_puertas : NumeroDePuertas
                 ) -> None:
        self.precio_base = precio_base
        self.precio_venta= 0
        self.numero_de_puertas = numero_de_puertas
        self.caballos_fuerza = caballos_fuerza
        self.numero_de_puestos = numero_de_puestos



    def calcularPrecio(self) -> None:
        porcentaje_por_numero_de_puertas = float(self.numero_de_puertas.value/100)
        porcentaje_por_numero_de_puestos = float(self.numero_de_puestos.value/100)
        self.precio_venta = self.precio_base + (self.precio_base * porcentaje_por_numero_de_puertas)
        + (self.precio_base * porcentaje_por_numero_de_puestos)

    def cambiarEstado(self,estado : StateCarConseccionario) -> None:
          self.estado = estado

    def verEstado(self) -> None:
         print("El estado del carro es",(self.estado.name))




# %%
car = CarConcesionario (precio_base = 50000000,
                  caballos_fuerza= 1000,
                  estado =StateCarConseccionario.CREADO,
                  numero_de_puestos = NumeroDePuestos.DOS_PUESTOS,
                  numero_de_puertas = NumeroDePuertas.DOS_PUERTAS)





# %%
car.calcularPrecio()
car.cambiarEstado(StateCarConseccionario.VENDIDO)

# %%

print(car.precio_venta)

print(car.precio_base)

car.verEstado()

# %% [markdown]
# Caso practico : Taller de carros

# %%
class StateCarTaller(Enum):
    REPARACION = 0
    REPARADO = 1
    INGRESADO = 2
    ENTREGADO  = 3


# %%
class TipoServicio (Enum) :

    MANTENIMIENTO = 10
    REPARACION = 10
    DIAGNOSTICO = 15


# %%
class CarTaller :
    def __init__(self, kilometraje: float,
                  hasRayaduras: bool,
                  estado :StateCarTaller,
                  descripcionConsulta : str,
                  valorBaseServicio : float,
                  tipoServicio : TipoServicio
                 ) -> None:
        self.kilometraje = kilometraje
        self.hasRayaduras= hasRayaduras
        self.estado = estado
        self.descripcionConsulta = descripcionConsulta
        self.valorBaseServicio = valorBaseServicio
        self.tipoServicio = tipoServicio
        self.totalValorServicio = 0



    def calcularPrecioServicio(self) -> None:
        porcentaje_por_tipo_de_reparacion = float(self.tipoServicio.value/100)
        self.totalValorServicio = self.valorBaseServicio + (self.valorBaseServicio * porcentaje_por_tipo_de_reparacion)

    def cambiarEstado(self,estado : StateCarTaller) -> None:
          self.estado = estado

    def verEstado(self) -> None:
         print("El estado del carro es",(self.estado.name))


# %%
carTaller = CarTaller(50000,False,StateCarTaller.INGRESADO,"El carro no pasa de 500 kilometros por horas",50000,TipoServicio.DIAGNOSTICO)

carTaller.calcularPrecioServicio()

carTaller.totalValorServicio

# %% [markdown]
# Implementando Interfaz

# %%

from abc import  abstractmethod
class Evaluar :

    @abstractmethod
    def ProbarEstado (self):
        pass
    @abstractmethod
    def MostrarAtributos(self):
        pass




# %%
class CarConcesionario (Evaluar) :
    def __init__(self, precio_base: float,
                  caballos_fuerza: int,
                  estado :StateCarConseccionario,
                  numero_de_puestos : NumeroDePuestos,
                  numero_de_puertas : NumeroDePuertas
                 ) -> None:
        self.precio_base = precio_base
        self.precio_venta= 0
        self.numero_de_puertas = numero_de_puertas
        self.caballos_fuerza = caballos_fuerza
        self.numero_de_puestos = numero_de_puestos



    def calcularPrecio(self) -> None:
        porcentaje_por_numero_de_puertas = float(self.numero_de_puertas.value/100)
        porcentaje_por_numero_de_puestos = float(self.numero_de_puestos.value/100)
        self.precio_venta = self.precio_base + (self.precio_base * porcentaje_por_numero_de_puertas)
        + (self.precio_base * porcentaje_por_numero_de_puestos)

    def cambiarEstado(self,estado : StateCarConseccionario) -> None:
          self.estado = estado

    def verEstado(self) -> None:
         print("El estado del carro es",(self.estado.name))

    def ProbarEstado(self):
         print("Se realizan las pruebas del carro antes de venderlo")
    def MostrarAtributos(self):
         print("Se muestran los atributos del carro")

# %%
class CarTaller (Evaluar) :
    def __init__(self, kilometraje: float,
                  hasRayaduras: bool,
                  estado :StateCarTaller,
                  descripcionConsulta : str,
                  valorBaseServicio : float,
                  tipoServicio : TipoServicio
                 ) -> None:
        self.kilometraje = kilometraje
        self.hasRayaduras= hasRayaduras
        self.estado = estado
        self.descripcionConsulta = descripcionConsulta
        self.valorBaseServicio = valorBaseServicio
        self.tipoServicio = tipoServicio
        self.totalValorServicio = 0



    def calcularPrecioServicio(self) -> None:
        porcentaje_por_tipo_de_reparacion = float(self.tipoServicio.value/100)
        self.totalValorServicio = self.valorBaseServicio + (self.valorBaseServicio * porcentaje_por_tipo_de_reparacion)

    def cambiarEstado(self,estado : StateCarTaller) -> None:
          self.estado = estado

    def verEstado(self) -> None:
         print("El estado del carro es",(self.estado.name))

    def ProbarEstado(self):
        print("Se realizan las pruebas del carro antes de entregarlo al cliente que lo trajo al taller")
    def MostrarAtributos(self):
         print("Se muestran los atributos del carro")




# %% [markdown]
# Herencia

# %%
class Vehiculo:
    def __init__(self,numero_de_llantas:int,numero_de_asientos:int,color:str) -> None:
        self.numero_de_llantas = numero_de_llantas
        self.numero_de_asientos = numero_de_asientos
        self.color = color
        pass
    def encender():
        print("El vehiculo enciende")

    def apagar():
        print("Apagando el vehiculo")

    def mostrarCombustible():
        print("Se muestra el nivel de combustible")





# %%
class Carro (Vehiculo):
    def __init__(self, numero_de_llantas: int, numero_de_asientos: int, color: str):
        super().__init__(numero_de_llantas, numero_de_asientos, color)

    def mostrarNivelDeCombustible():
        print("Se muestra nivel de combustible")


# %%
class Moto (Vehiculo):
    def __init__(self, numero_de_llantas: int, numero_de_asientos: int, color: str) -> None:
        super().__init__(numero_de_llantas, numero_de_asientos, color)

    def mostrarNivelDeCombustible():
        print("Se muestra nivel de combustible")


# %% [markdown]
# Polimorfismo

# %%
class CuidadosVehiculo:
    def HacerMantenimiento():
        pass
    def LavarVehiculo():
        pass

# %%
class Moto (CuidadosVehiculo) :
    def __init__(self, marca:str, modelo : str
                 ) -> None:
        self.marca = marca
        self.modelo = modelo

    def HacerMantenimiento():
         print("Se realiza un manteniemiento diferente")
    def LavarVehiculo():
         print("Se lava diferente")

# %%
class Car (CuidadosVehiculo) :
    def __init__(self, marca: str,modelo:str, chasis:str
                 ) -> None:
       self.marca= marca
       self.modelo = modelo
       self.chasis = chasis
    def HacerMantenimiento():
         print("Se realiza el matenimiento al carro")
    def LavarVehiculo():
         print("Se lava el carro")




