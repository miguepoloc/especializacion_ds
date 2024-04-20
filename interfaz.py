# %%
class vehiculo:
    def avanzar(self)->None:
        pass
    def frenar(self)->None:
        pass

# %%
class Carro(vehiculo):
    def avanzar(self) -> None:
        print("el carro avanza")
    def frenar(self) -> None:
        print("el carro se detiene")

# %%
carro=Carro()
carro.avanzar()
carro.frenar()

# %%
class Helicoptero(vehiculo):
    def avanzar(self) -> None:
        print("el helicoptero se eleva")
    def frenar(self) -> None:
        print("el helicoptero desciende")

# %%
helicoptero=Helicoptero()
helicoptero.avanzar()
helicoptero.frenar()


