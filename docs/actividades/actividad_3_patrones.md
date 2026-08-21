# Actividad 3 — Patrones de Diseño (50 pts)

## Qué se hace

A diferencia de POO y SOLID, aquí no completas un esqueleto: **eliges y escribes tú mismo** 3 patrones de diseño GoF de los 23 vistos en clase (carpeta `patrones/`), uno de cada categoría:

- 1 patrón **creacional** (de los 5: Factory Method, Abstract Factory, Builder, Prototype, Singleton)
- 1 patrón **estructural** (de los 7: Adapter, Bridge, Composite, Decorator, Facade, Flyweight, Proxy)
- 1 patrón **de comportamiento** (de los 11: Chain of Responsibility, Command, Interpreter, Iterator, Mediator, Memento, Observer, State, Strategy, Template Method, Visitor)

Para cada uno de los 3, escribe un notebook siguiendo el mismo formato que ya viste en `patrones/` (puedes usar cualquier notebook de esa carpeta como plantilla de estructura):

1. Breve introducción: qué problema resuelve el patrón elegido.
2. Código **"sin patrón"**: un ejemplo donde el problema es evidente.
3. Código **"con patrón"**: la misma situación resuelta aplicando el patrón, ejecutando ambos para que se vea el contraste.
4. Un diagrama UML simple del patrón aplicado (puedes usar Graphviz o PlantUML, como en `class_uml/`).
5. Una explicación corta de **por qué elegiste ese patrón y no otro** para ese problema.

No repitas literal los ejemplos que ya viste en clase — usa un problema propio o adaptado, aunque sea inspirado en uno visto.

## Mínimos exigidos

- Cada patrón debe implementar **todos los roles estructurales que le corresponden** (ej. Strategy: contexto + interfaz de estrategia + al menos 2 estrategias concretas; Factory Method: creador + al menos 2 productos concretos; Observer: sujeto + al menos 2 observadores concretos) — no basta con nombrar el patrón en un comentario.
- El código "con patrón" debe ejecutar sin errores.
- El diagrama UML debe reflejar los nombres reales de tus clases (no un diagrama genérico copiado de la teoría).

Entregas por debajo de estos mínimos se evalúan igual con la rúbrica, pero no pueden superar el nivel "Aceptable" en la(s) dimensión(es) afectada(s).

## Qué se entrega

3 notebooks (uno por patrón elegido), dentro de tu carpeta:

```
entregas/<tu_codigo_estudiante>/actividad_3_patrones/
  <patron_creacional_elegido>.ipynb
  <patron_estructural_elegido>.ipynb
  <patron_comportamiento_elegido>.ipynb
```

Nombra cada archivo con el nombre del patrón en minúsculas (ej. `builder.ipynb`, `adapter.ipynb`, `strategy.ipynb`).

## Cómo se entrega

1. Rama propia: `entrega/<tu_codigo>-actividad3-patrones`.
2. Crea tu carpeta en `entregas/` con los 3 notebooks.
3. Pull Request con título `Actividad 3 - Patrones - <Tu Nombre>`.
4. Trabajo **individual**.

## Cuándo

Se entrega el **sábado del Fin de Semana 3** (al cierre de la sesión de Patrones de Comportamiento, con la que termina el bloque completo de patrones), antes de finalizar el día.

## Cómo se califica

Rúbrica completa: [`docs/rubricas/patrones.md`](../rubricas/patrones.md) — 3 dimensiones (una por patrón/categoría, 12 pts c/u) + contraste sin/con patrón (8 pts) + documentación y justificación (6 pts) = 50 pts, con 4 niveles de desempeño por dimensión. Puede evaluarse con asistencia de IA — ver [`docs/rubricas/README.md`](../rubricas/README.md).
