class MySQLDatabase:
    def guardar_registro(self, data):
        print(f"[MySQL Concreto] Guardando: {data}")

class ServicioPedidosBad:
    def __init__(self):
        # Acoplamiento directo dentro del constructor
        self.db = MySQLDatabase()

    def registrar_orden(self, cliente, total):
        info = f"Orden de {cliente} - Total: ${total}"
        self.db.guardar_registro(info)

bad_service = ServicioPedidosBad()
bad_service.registrar_orden("Daniel", 120000)