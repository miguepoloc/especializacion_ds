class Pedido:
    def __init__(self, cliente, items):
        self.cliente = cliente
        self.items = items

    def calcular_total(self) -> float:
        return sum(item["precio"] * item.get("cantidad", 1) for item in self.items)

class RepositorioPedido:
    def guardar(self, pedido: Pedido):
        print(f"[BD] Guardando pedido de '{pedido.cliente}' por ${pedido.calcular_total():.2f}...")

class ServicioNotificacion:
    def enviar_confirmacion(self, pedido: Pedido):
        print(f"[EMAIL] Notificación enviada a '{pedido.cliente}' por su pedido.")

# Uso modular
pedido = Pedido("Daniel", [{"precio": 150000, "cantidad": 1}, {"precio": 45000, "cantidad": 2}])
repo = RepositorioPedido()
notificador = ServicioNotificacion()

repo.guardar(pedido)
notificador.enviar_confirmacion(pedido)