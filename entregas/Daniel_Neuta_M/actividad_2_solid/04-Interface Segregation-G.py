from abc import ABC, abstractmethod
class ProcesableEnLinea(ABC):
    @abstractmethod
    def pagar_digital(self, monto: float): pass

class RequiereEnvio(ABC):
    @abstractmethod
    def coordinar_despacho(self, direccion: str): pass

class Facturable(ABC):
    @abstractmethod
    def emitir_comprobante(self): pass

# Cliente Digital: usa pago online, despacho y factura
class ClienteTiendaOnline(ProcesableEnLinea, RequiereEnvio, Facturable):
    def pagar_digital(self, monto: float):
        print(f"Pago electrónico procesado por ${monto:.2f}")

    def coordinar_despacho(self, direccion: str):
        print(f"Guía de envío creada hacia: {direccion}")

    def emitir_comprobante(self):
        print("Factura electrónica enviada al correo.")

# Cliente Físico: solo requiere comprobante directo
class ClienteRetiroLocal(Facturable):
    def emitir_comprobante(self):
        print("Ticket de caja impreso.")

# Uso
cliente_web = ClienteTiendaOnline()
cliente_web.pagar_digital(150000.0)
cliente_web.coordinar_despacho("Carrera 5 # 10-20")

cliente_local = ClienteRetiroLocal()
cliente_local.emitir_comprobante()