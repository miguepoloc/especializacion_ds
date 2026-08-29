from abc import ABC, abstractmethod
class CalculadorDescuentoBad:
    def aplicar(self, total, tipo_cliente):
        if tipo_cliente == "Estudiante":
            return total * 0.90  # 10% rígido
        elif tipo_cliente == "Profesor":
            return total * 0.85  # 15% rígido
        elif tipo_cliente == "VIP":
            return total * 0.80  # 20% rígido
        else:
            return total

calc_bad = CalculadorDescuentoBad()
print("Total (Bad):", calc_bad.aplicar(200000, "Estudiante"))