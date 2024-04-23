class Humanito:
    def __init__(self, nombre, edad, estado) -> None:
        self.Nombre = nombre
        self.Edad = edad
        self.vida = estado

    def CMurio(self,motivo):
        self.vida = 0
        print(f"Nivel de sangre caliente: {self.vida}%")
        print(f"SE MURIO POR:   {motivo}. A la edad de {self.Edad}")

    def CEmborracho(self,motiva):
        print(f"{self.Nombre} se emborracho por:   {motiva}")

class HumanitoQueEstudia(Humanito):
    def __init__(self, nombre:str , edad, estado, estudia, monedas):
        super().__init__(nombre, edad, estado)
        self.Estudia = estudia
        self.__Dinero = monedas

    def CMurio(self, motivo):
        print(f"{self.Nombre} estudiante de {self.Estudia} se murio")
        return super().CMurio(motivo)

    def CEmborracho(self, motiva):
        return super().CEmborracho(motiva)
    
    def CuantoDinero(self):
        return self.__Dinero

    def Robado(self, saldo):
        self.__Dinero-= saldo


class HumanitoQueRoba(Humanito):
    def __init__(self, nombre, edad, estado, arma, Bolsillo) -> None:
        super().__init__(nombre, edad, estado)
        self.Arma = arma
        self.CapacidadBolsillo = Bolsillo

    def Mata(self, motivo, HumanitoQueEstudia):
        HumanitoQueEstudia.CMurio(motivo)
        print(f"{self.Nombre} con {self.Edad} de edad, mato a {HumanitoQueEstudia.Nombre} estudiante de {HumanitoQueEstudia.Estudia} con {self.Arma}")

    def RobaInteligentemente(self, HumanitoQueEstudia):
        print()
        print(f"- Hola {HumanitoQueEstudia.Nombre}, si tuvieras que decirme cuanto dinero tienes qué valor me dirias?")
        print(f"- {HumanitoQueEstudia.CuantoDinero()}, obviamente")
        self.CapacidadBolsillo = HumanitoQueEstudia.CuantoDinero()
        HumanitoQueEstudia.Robado(HumanitoQueEstudia.CuantoDinero())
        print()
        print("- Matanga dijo la Changa! ")

humanitoEstudioso = HumanitoQueEstudia("Humanito", 12, False, "Python", 100)
humanitoEstudioso.CEmborracho("se aburrio")

humanitoLadron = HumanitoQueRoba("Humanito Malo", 12, False, "Corta Uña", 0)
humanitoLadron.Mata("estaba aburrido", humanitoEstudioso)