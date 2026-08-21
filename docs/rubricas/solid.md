# Rúbrica — Actividad 2: Principios SOLID (50 pts)

Enunciado oficial de la actividad: [`docs/actividades/actividad_2_solid.md`](../actividades/actividad_2_solid.md) — completar los 5 notebooks de `solid/ejercicios/`.

Corresponde 1:1 con los 5 notebooks de `solid/`: `single_responsibility.ipynb`, `open_closed.ipynb`, `liskov.ipynb`, `interface_segregation.ipynb`, `dependency_inversion.ipynb`.

## Resumen de dimensiones

| Dimensión | Puntos máximos |
|---|---|
| 1. Single Responsibility (SRP) | 10 |
| 2. Open/Closed (OCP) | 10 |
| 3. Liskov Substitution (LSP) | 10 |
| 4. Interface Segregation (ISP) | 10 |
| 5. Dependency Inversion (DIP) | 10 |
| **Total** | **50** |

Para cada principio se espera, idealmente, un contraste **"sin el principio" → "con el principio"** (como el patrón pedagógico de `liskov.ipynb`), aunque no es obligatorio si el ejemplo aplicado desde cero ya es suficientemente claro.

## 1. Single Responsibility (10 pts)

| Nivel | Puntos | Descriptor |
|---|---|---|
| Excelente | 9-10 | Cada clase tiene una única razón para cambiar; el ejemplo muestra una clase "God object" dividida en clases con responsabilidades separadas, y explica en texto/comentario cuál es la única responsabilidad de cada una. |
| Bueno | 7-8 | Las clases están razonablemente separadas por responsabilidad, pero al menos una mezcla dos responsabilidades no relacionadas (ej. lógica de negocio + persistencia en la misma clase). |
| Aceptable | 5-6 | Hay más de una clase, pero la división no responde claramente a "razones para cambiar" — parece arbitraria. |
| Insuficiente | 0-4 | Una sola clase/función hace todo (validación, lógica, entrada/salida) sin ninguna separación. |

## 2. Open/Closed (10 pts)

| Nivel | Puntos | Descriptor |
|---|---|---|
| Excelente | 9-10 | Añadir un nuevo caso (tipo, comportamiento) no requiere modificar código existente — se logra vía herencia/polimorfismo o inyección de una nueva implementación, y el ejemplo demuestra explícitamente "agregar X sin tocar Y". |
| Bueno | 7-8 | Usa herencia/abstracción para extender comportamiento, pero el ejemplo no demuestra explícitamente el caso de extensión (queda implícito). |
| Aceptable | 5-6 | Hay algún intento de abstracción, pero extender el comportamiento seguiría requiriendo tocar la clase base (ej. `if/elif` que crece). |
| Insuficiente | 0-4 | Cualquier cambio de comportamiento requiere editar directamente la clase/función existente; no hay punto de extensión. |

## 3. Liskov Substitution (10 pts)

| Nivel | Puntos | Descriptor |
|---|---|---|
| Excelente | 9-10 | Muestra una subclase que SÍ es sustituible (mantiene el contrato del padre) Y un contraejemplo que lo viola (cambia tipo de retorno, lanza excepción inesperada, o fortalece precondiciones) — como el patrón BMW/Chevrolet de `liskov.ipynb`, con el error resultante explicado. |
| Bueno | 7-8 | Solo muestra el caso correcto (subclase sustituible) sin contraejemplo, pero la explicación en texto es clara sobre por qué cumple LSP. |
| Aceptable | 5-6 | Hay herencia, pero no se verifica ni se discute la sustituibilidad — no queda claro si viola o no LSP. |
| Insuficiente | 0-4 | La subclase rompe visiblemente el contrato del padre (tipo de retorno distinto, excepción no esperada) y esto no se identifica como problema en el ejemplo. |

## 4. Interface Segregation (10 pts)

| Nivel | Puntos | Descriptor |
|---|---|---|
| Excelente | 9-10 | Contrasta una interfaz "gorda" (obliga a implementar métodos irrelevantes) con su versión segregada en interfaces más pequeñas y específicas; el cliente solo depende de lo que usa. |
| Bueno | 7-8 | Hay interfaces pequeñas y específicas, pero sin mostrar el problema que resuelven (falta el "antes"). |
| Aceptable | 5-6 | Existe una interfaz, pero es única y relativamente amplia — no se explora la segregación. |
| Insuficiente | 0-4 | Una interfaz/clase base obliga a las subclases a implementar métodos que no necesitan (ej. `raise NotImplementedError` en varios métodos no usados), sin abordar el problema. |

## 5. Dependency Inversion (10 pts)

| Nivel | Puntos | Descriptor |
|---|---|---|
| Excelente | 9-10 | Una clase de alto nivel depende de una abstracción (interfaz/clase abstracta), no de una implementación concreta; la implementación concreta se inyecta (constructor, parámetro) y puede sustituirse sin tocar la clase de alto nivel. |
| Bueno | 7-8 | Hay una abstracción de por medio, pero la clase de alto nivel instancia directamente la implementación concreta en vez de recibirla inyectada. |
| Aceptable | 5-6 | Se menciona/discute el concepto pero el ejemplo de código no evidencia inversión real (la dependencia sigue siendo concreta). |
| Insuficiente | 0-4 | La clase de alto nivel depende directamente de una clase de bajo nivel concreta, sin ninguna abstracción intermedia. |
