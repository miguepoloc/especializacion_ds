class Relacion:
    def __init__(self):
        self.__mujer = "Sutanita"  # Realizamos encapsulación del atributo
        self.__moza = "Esperenzajita"  # Realizamos encapsulación del atributo

    def llama_mujer(self) -> str:
        return f"Llamar normalmente a {self.__mujer}"

    def __llamar_moza_en_calle(self) -> str:
        return f"Llamar a escondidas a {self.__moza}"

final = Relacion()

print(final.llama_mujer())