# %% [markdown]
# Arrendamiento de casa

# %%
class casa:
    def __init__(self,numero_de_habitaciones:int, valor_arriendo:int ) -> None:
        self.numero_de_habitaciones=numero_de_habitaciones
        self.valor_arriendo=valor_arriendo



    def __str__(self) -> str:
        return f"Numero de Habitaciones:{self.numero_de_habitaciones} , valor arriendo {self.valor_arriendo} "


# %%
arrendar=casa(numero_de_habitaciones=3, valor_arriendo=200000)
print(arrendar)

# %% [markdown]
# construccion de casa

# %%
class casa:
    def __init__(self, cemento:int,area:int, bloques:int ) -> None:
        self.cemento=cemento
        self.area=area
        self.bloques=bloques



    def __str__(self) -> str:
        return f"Cemento:{self.cemento} ,Area a construir:{self.area}, cantidad de Bloques: {self.bloques} "



# %%
construir=casa(cemento=50, area=68, bloques=2000)
print(construir)


