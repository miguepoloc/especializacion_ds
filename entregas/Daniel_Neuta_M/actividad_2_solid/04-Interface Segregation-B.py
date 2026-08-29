from abc import ABC, abstractmethod
class OperacionesPedidoBad(ABC):
    @abstractmethod
    def pagar_pse(self): pass

    @abstractmethod
    def generar_factura_electronica(self): pass

    @abstractmethod
    def solicitar_despacho_envio(self): pass

class ClienteMostradorBad(OperacionesPedidoBad):
    def pagar_pse(self):
        pass 

    def generar_factura_electronica(self):
        print("Imprimiendo recibo térmico simple...")

    def solicitar_despacho_envio(self):
        pass