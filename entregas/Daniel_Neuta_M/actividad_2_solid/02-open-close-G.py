from abc import ABC, abstractmethod
class Descuento(ABC):
    @abstractmethod
    def aplicar(self, total: float) -> float:
        pass

class DescuentoPorcentaje(Descuento):
    def __init__(self, porcentaje: float):
        # Recibe dinámicamente cualquier porcentaje (ej: 10, 12.5, 30)
        self.porcentaje = porcentaje

    def aplicar(self, total: float) -> float:
        return total * (1 - (self.porcentaje / 100))

class DescuentoMontoFijo(Descuento):
    def __init__(self, monto: float):
        self.monto = monto

    def aplicar(self, total: float) -> float:
        return max(0.0, total - self.monto)

class SinDescuento(Descuento):
    def aplicar(self, total: float) -> float:
        return total

# Uso dinámico: abierto a extensión, cerrado a modificación
total_base = 200000.0

desc_estudiante = DescuentoPorcentaje(porcentaje=10)
desc_black_friday = DescuentoPorcentaje(porcentaje=35)
desc_cupon = DescuentoMontoFijo(monto=25000)

print(f"Total Estudiante (10%): ${desc_estudiante.aplicar(total_base):.2f}")
print(f"Total Black Friday (35%): ${desc_black_friday.aplicar(total_base):.2f}")
print(f"Total Cupón ($25.000): ${desc_cupon.aplicar(total_base):.2f}")