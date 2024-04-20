# %%
class vehiculo():
    def __init__(self,tipo:str) -> None:
        self.tipo=tipo
    def movimiento(self)->None:
        pass
    def describeme(self)->None:
        print("soy un vehiculo tipo", type(self).__name__)




# %%
class Carro(vehiculo):
    pass
carro=Carro("terrestre")
carro.describeme()

# %%
class Carro(vehiculo):
    def movimiento(self) -> None:
        print("avanzar")

    def describeme(self) -> None:
        print("terrestre")


class Helicoptero(vehiculo):
    def movimiento(self) -> None:
        print("elevarse")

    def describeme(self) -> None:
        print("aereo")

# %%
helicoptero=Helicoptero("aereo")
helicoptero.movimiento()


