class MetodoPagoBad:
    def procesar_transaccion_online(self, monto):
        print(f"Procesando pago en línea de ${monto}...")

class PagoTarjetaBad(MetodoPagoBad):
    def procesar_transaccion_online(self, monto):
        print(f"Cobro web exitoso de ${monto} a la tarjeta.")

class PagoEfectivoPuntoBad(MetodoPagoBad):
    def procesar_transaccion_online(self, monto):
        raise NotImplementedError("El pago en efectivo no soporta procesamiento web")

metodos = [PagoTarjetaBad(), PagoEfectivoPuntoBad()]
for m in metodos:
    m.procesar_transaccion_online(50000)