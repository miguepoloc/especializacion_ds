from abc import ABC, abstractmethod
class MetodoPago(ABC):
    @abstractmethod
    def procesar_pago(self, monto: float) -> bool:
        pass

class PagoTarjeta(MetodoPago):
    def __init__(self, franquicia: str):
        self.franquicia = franquicia

    def procesar_pago(self, monto: float) -> bool:
        print(f"[TARJETA {self.franquicia}] Procesado cobro por ${monto:.2f}")
        return True

class PagoTransferencia(MetodoPago):
    def __init__(self, banco: str):
        self.banco = banco

    def procesar_pago(self, monto: float) -> bool:
        print(f"[TRANSFERENCIA {self.banco}] Transacción aprobada por ${monto:.2f}")
        return True

def finalizar_compra(metodo: MetodoPago, monto: float):
    if metodo.procesar_pago(monto):
        print("-> Orden completada con éxito.\n")

finalizar_compra(PagoTarjeta("VISA"), 180000.0)
finalizar_compra(PagoTransferencia("Bancolombia"), 180000.0)