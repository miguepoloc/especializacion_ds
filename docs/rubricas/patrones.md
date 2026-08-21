# Rúbrica — Actividad 3: Patrones de Diseño (50 pts)

Enunciado oficial de la actividad: [`docs/actividades/actividad_3_patrones.md`](../actividades/actividad_3_patrones.md) — el estudiante aplica **3 patrones, uno de cada categoría GoF** (creacional, estructural, de comportamiento), elegidos libremente entre los 23 vistos en clase.

## Resumen de dimensiones

| Dimensión | Puntos máximos |
|---|---|
| 1. Patrón creacional aplicado | 12 |
| 2. Patrón estructural aplicado | 12 |
| 3. Patrón de comportamiento aplicado | 12 |
| 4. Contraste "sin patrón / con patrón" | 8 |
| 5. Documentación y justificación | 6 |
| **Total** | **50** |

## 1-3. Patrón por categoría (12 pts cada uno — mismo criterio para creacional/estructural/comportamiento)

| Nivel | Puntos | Descriptor |
|---|---|---|
| Excelente | 11-12 | El patrón resuelve un problema real planteado en el ejemplo (no está "pegado" sin necesidad); la estructura de clases sigue fielmente el patrón (roles correctos: ej. en Factory Method existe el método de fábrica sobrescribible por subclases, no un simple `if/elif`). |
| Bueno | 8-10 | El patrón está correctamente implementado en su estructura, pero el problema que resuelve es artificial/trivial (no queda claro por qué se necesitaba el patrón). |
| Aceptable | 5-7 | Usa el nombre del patrón y algunas piezas de su estructura, pero le falta algún rol clave o el comportamiento no corresponde realmente al patrón (ej. "Factory" que es solo una función con `if/elif`, sin punto de extensión). |
| Insuficiente | 0-4 | No hay evidencia real del patrón (solo se menciona en un comentario/texto) o el patrón elegido no corresponde a la categoría exigida. |

## 4. Contraste "sin patrón / con patrón" (8 pts)

| Nivel | Puntos | Descriptor |
|---|---|---|
| Excelente | 7-8 | Para al menos uno de los 3 patrones, muestra explícitamente el código "antes" (sin el patrón, con el problema visible) y "después" (con el patrón, problema resuelto) — replicando el formato pedagógico de `patrones/`. |
| Bueno | 5-6 | Explica en texto qué problema resolvía la ausencia del patrón, pero sin código "antes" ejecutable. |
| Aceptable | 3-4 | Menciona brevemente la motivación del patrón sin contraste claro antes/después. |
| Insuficiente | 0-2 | No hay ninguna explicación de qué problema resuelve cada patrón frente a no usarlo. |

## 5. Documentación y justificación (6 pts)

| Nivel | Puntos | Descriptor |
|---|---|---|
| Excelente | 6 | Cada patrón tiene una explicación breve (markdown/comentario) de por qué se eligió ese patrón y no otro para el problema planteado. |
| Bueno | 4-5 | Hay documentación básica (qué patrón es) pero no una justificación de la elección. |
| Aceptable | 2-3 | Documentación mínima o genérica (copiada de la definición del patrón, sin conectarla al ejemplo propio). |
| Insuficiente | 0-1 | Sin ninguna documentación ni comentario. |
