from abc import ABC, abstractmethod
class ConexionBaseDatos(ABC):
    @abstractmethod
    def guardar_registro(self, data: str):
        pass

# Implementaciones concretas de bajo nivel
class EngineMySQL(ConexionBaseDatos):
    def guardar_registro(self, data: str):
        print(f"[Engine MySQL] Registro guardado en BD Relacional: {data}")

class EnginePostgreSQL(ConexionBaseDatos):
    def guardar_registro(self, data: str):
        print(f"[Engine PostgreSQL] Registro guardado en servidor remoto: {data}")

# Módulo de alto nivel: No le importa qué BD se use mientras cumpla el contrato
class ServicioPedidos:
    def __init__(self, db: ConexionBaseDatos):
        # Inyección de dependencias
        self.db = db

    def registrar_orden(self, cliente: str, total: float):
        payload = f"Cliente: {cliente} | Valor: ${total:.2f}"
        self.db.guardar_registro(payload)

# Uso flexible e intercambiable
db_mysql = EngineMySQL()
servicio_a = ServicioPedidos(db_mysql)
servicio_a.registrar_orden("Daniel", 120000.0)

db_postgres = EnginePostgreSQL()
servicio_b = ServicioPedidos(db_postgres)
servicio_b.registrar_orden("Daniel", 120000.0)