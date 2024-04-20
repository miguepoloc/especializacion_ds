# %%
class vehiculo:
    def movimiento(self):
        pass


class carro(vehiculo):
    def movimiento(self):
        print("avanzar")

class helicoptero(vehiculo):
    def movimiento(self):
        print("elevarse")





# %%
for vehiculo in carro(), helicoptero():
    vehiculo.movimiento()


