class Relacion:
    Mujer = "Sutanita"  # Accesible desde el exterior
    __Moza = "Esperenzajita"  # No accesible

    # No accesible desde el exterior
    def __llamar_moza_en_calle(self) -> None:
        return f"Llamar a escondidas a {self.__Moza}"


    # Accesible desde el exterior
    def llama_mujer(self) -> None:
        # El método si es accesible desde el interior
        return f"Llamar normalmente a {self.Mujer}"

final = Relacion()

final.llama_mujer