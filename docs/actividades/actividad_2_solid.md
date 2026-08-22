# Actividad 2 — Principios SOLID (50 pts)

## Qué se hace

Usando un problema propio (puedes reutilizar y evolucionar el dominio de la Actividad 1, o elegir uno nuevo), demuestra los 5 principios SOLID con tu propio diseño. Para **cada uno de los 5 principios**, muestra el contraste:

- Un fragmento de código que **viola** el principio (con el problema visible: qué se rompe si sigues agregando funcionalidad así).
- La versión **corregida**, aplicando el principio, resolviendo ese problema concreto.

| Principio | Qué debes evidenciar |
|---|---|
| S — Responsabilidad Única | Una clase con >1 responsabilidad → dividida en clases con una responsabilidad cada una |
| O — Abierto/Cerrado | Agregar un caso nuevo requiere modificar código existente → rediseño donde se extiende sin modificar |
| L — Sustitución de Liskov | Una subclase que rompe el contrato del padre → una que sí es sustituible |
| I — Segregación de Interfaces | Una interfaz "gorda" que obliga a implementar métodos innecesarios → interfaces segregadas |
| D — Inversión de Dependencias | Una clase de alto nivel dependiendo de una concreta → dependiendo de una abstracción |

No repitas literal los ejemplos de clase (Book, Shape, Worker/Eater, etc.) — aplícalo a tu propio dominio.

## Mínimos exigidos

- Los 5 contrastes deben ser **código real y ejecutable** (clases con métodos reales), no pseudocódigo ni solo texto explicando el principio.
- Cada clase involucrada debe tener **al menos 2 métodos y 2 atributos** — nada de clases de una sola línea que "simulan" el problema sin mostrarlo de verdad.
- El código "con el principio aplicado" debe ejecutar sin errores.

Entregas por debajo de estos mínimos se evalúan igual con la rúbrica, pero no pueden superar el nivel "Aceptable" en la(s) dimensión(es) afectada(s).

Diagrama UML: **no es obligatorio** en esta actividad (a diferencia de POO y Patrones) — SOLID trata más sobre relaciones de dependencia/contrato entre clases que sobre estructura general. Puedes incluirlo si quieres, se valorará como plus dentro de "Calidad" pero no es requisito.

## Qué se entrega

Un notebook (o uno por principio, como prefieras) con los 5 contrastes "viola/cumple", ejecutados, dentro de tu carpeta:

```
entregas/<tu_nombre_estudiante>/actividad_2_solid/
  solid.ipynb   # o 5 notebooks, uno por principio
```

**Nota**: los notebooks de `solid/ejercicios/` (con TODO para completar) son material de **práctica opcional** — no son el entregable.

## Cómo se entrega

1. Rama propia: `entrega/<tu_nombre>-actividad2-solid`.
2. Crea tu carpeta en `entregas/` con tu(s) notebook(s).
3. Pull Request con título `Actividad 2 - SOLID - <Tu Nombre>`.
4. Trabajo **individual**.

## Cuándo

Se entrega el **sábado del Fin de Semana 2** (el mismo día que se dicta la segunda mitad de SOLID: I, D), antes de finalizar el día.

## Cómo se califica

Rúbrica completa: [`docs/rubricas/solid.md`](../rubricas/solid.md) — 5 dimensiones (un principio cada una, 10 pts), 4 niveles de desempeño por dimensión. Puede evaluarse con asistencia de IA — ver [`docs/rubricas/README.md`](../rubricas/README.md).
