# Guía de clase en vivo — Auditoría de `weather_station`

Material de apoyo para una sesión de clase donde los estudiantes practican **detectar** code smells, violaciones SOLID y patrones mal aplicados sobre un proyecto real (no un ejemplo de juguete). Repo: `github.com/miguepoloc/weather_station` (backend FastAPI + PostgreSQL de una estación climática IoT, en producción sobre Fly.io).

Formato sugerido: proyecta el código en vivo, haz la pregunta de cada bloque ANTES de revelar el hallazgo/respuesta, deja que los estudiantes propongan el patrón/solución antes de mostrar la sugerida.

**No es parte de la evaluación** — es demo de clase. Los estudiantes refactorizan su propio código en la Actividad 4, no este repo.

---

## 0. Contexto para presentar (2 min)

Es un backend real, desplegado en producción (Docker + Fly.io + CI en `.github/workflows/fly.yml`), no un ejemplo diseñado a propósito para fallar. Tiene 3 dominios: `nodes/` (sensores), `data/` (telemetría), `users/` (auth). El propio autor fue añadiendo patrones "de práctica" commit a commit sin terminar de integrarlos — es deuda técnica auténtica.

## 1. Cuatro formas de conectar a la base de datos

Muestra `src/database.py`, `src/database_adapter.py`, `src/database_bridge.py`, `src/database_fly_weight.py`.

**Pregunta:** ¿por qué hay 4 archivos que hacen básicamente lo mismo? ¿Qué principio SOLID se viola?

**Hallazgo:** `data/router.py` usa `database.py`, `nodes/router.py` usa `database_adapter.py`, y `database_bridge.py`/`database_fly_weight.py` no los usa nadie (código muerto). Viola **DIP** — los routers dependen de clases concretas, no de una abstracción común.

**Bug escondido (buen "gotcha" para la clase):** en 3 de los 4 archivos, un método:
```python
def session(self):
    return self.session()
```
Un atributo de instancia `self.session = sessionmaker(...)` sobrescribe al método `session()` definido más abajo en la misma clase — funciona "por accidente" porque el atributo gana la resolución de nombre. Pregunta a la clase: *¿alguien puede explicar por qué esto no entra en recursión infinita?*

**Patrón sugerido:** Abstract Factory o Factory Method consolidando las 4 en una sola fuente de verdad.

## 2. El endpoint que hace demasiado

Muestra `src/data/router.py`, función `save_data` (~líneas 38-66).

**Pregunta:** ¿cuántas responsabilidades distintas tiene esta única función? Cuéntenlas en voz alta.

**Hallazgo:** mapea 15 campos Pydantic→ORM a mano, persiste, construye el `NodeSubject` del patrón Observer, registra observadores concretos, y dispara la notificación — todo en un handler HTTP. Viola **SRP**.

**Bonus:** se importa `EmailObserver` pero nunca se usa (`router.py` solo adjunta `ConsoleObserver` y `SmsObserver`). El observer "documentado" en el código nunca dispara en producción — buen ejemplo de feature a medio integrar.

**Patrón ya presente pero mal ubicado:** Observer. Discusión: ¿dónde debería vivir la configuración de qué observadores se adjuntan?

## 3. Copiar y pegar 33 líneas dos veces

Muestra `src/data/strategy.py`: `HoursNodesData.get_nodes_data` vs `DaysNodesData.get_nodes_data`.

**Pregunta:** ¿qué pasa si mañana agregamos un nuevo sensor (un campo más)? ¿Cuántos lugares del código hay que tocar?

**Hallazgo:** las dos clases son casi idénticas — mismo bloque de 13 promedios repetido. Agregar un campo obliga a tocar `models.py`, `schemas.py`, y **cada** estrategia. Viola **OCP** y **DRY**, aunque el patrón Strategy ya está "puesto".

**Discusión clave:** usar el nombre del patrón no es lo mismo que cumplir su intención — aquí Strategy está aplicado pero mal implementado (el algoritmo variable no está realmente aislado del código repetido).

## 4. Una fábrica que no es extensible

Muestra `src/nodes/factory.py`, función `create_node` (~líneas 29-39).

**Pregunta:** si mañana aparece un tercer `NodeType`, ¿qué hay que modificar?

**Hallazgo:** `if type_node == NodeType.MASTER: ... elif ...: ... else: raise ValueError` — cada tipo nuevo obliga a editar la fábrica existente. Viola **OCP**. Es el mismo caso que el punto 1: el patrón "Factory" está nombrado pero no cumple su propósito de extensibilidad.

## 5. Un bug de copiar y pegar real

Muestra `src/models.py`, clase `User` (~líneas 95-112).

**Pregunta:** lean las dos secciones de atributos de esta clase con cuidado. ¿Notan algo?

**Hallazgo:** `first_name`, `last_name`, `document`, etc. están declarados **dos veces** en la misma clase. No es un ejemplo forzado — es un bug real de copy-paste. Sirve para mostrar que la duplicación no es solo "estética", puede esconder errores.

## 6. Seguridad que existe pero no se usa

Muestra `src/authorizer.py` (bien construido, con `get_current_user`, `Authorizer`, `Hasher`) vs. los routers de `/nodes` y `/data`.

**Pregunta:** ¿quién puede leer o escribir datos de sensores en este sistema?

**Hallazgo:** ningún router de `/nodes` o `/data` usa `Depends(get_current_user)` — cualquiera, sin token, puede leer/escribir. La abstracción está bien construida pero no conectada al resto del sistema.

**Patrón sugerido:** Decorator (o dependencia transversal) para aplicar autorización sin repetir código en cada endpoint.

## 7. Cierre de la sesión (5 min)

Pregunta final a la clase: de los 5-6 problemas vistos, **¿cuáles ya tenían un patrón GoF aplicado (aunque mal) y cuáles no tenían ninguno?** — Respuesta: 1, 2, 3 y 4 tienen intentos de patrón mal aplicados (Abstract Factory/Bridge/Flyweight, Observer, Strategy, Factory Method); 5 y 6 no tienen ningún patrón, son smells "crudos". Esto conecta con la Actividad 4: en su propio proyecto van a encontrarse con ambos casos — código sin ningún patrón, y código con un patrón aplicado a medias.

**Nota:** `src/tests/` solo tiene `__init__.py` — no hay pruebas en todo el proyecto. Vale la pena cerrar con esa reflexión: cualquier refactor "a ciegas" de este código es arriesgado sin antes escribir pruebas de caracterización — el mismo consejo aplica al proyecto de los estudiantes.
