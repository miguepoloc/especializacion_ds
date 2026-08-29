class GestionPedidosBad:
    def __init__(self, cliente, items):
        self.cliente = cliente
        self.items = items

    def procesar_pedido_completo(self):
        total = sum(item["precio"] * item.get("cantidad", 1) for item in self.items)

        print(f"[BD] Guardando pedido del cliente '{self.cliente}' por un total de ${total:.2f}...")

        print(f"[EMAIL] Enviando confirmación de compra a '{self.cliente}'...")
        return total

script_bad = GestionPedidosBad("Daniel", [{"precio": 150000, "cantidad": 1}, {"precio": 45000, "cantidad": 2}])
script_bad.procesar_pedido_completo()