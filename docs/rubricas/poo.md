# Rúbrica — Actividad 1: Programación Orientada a Objetos (50 pts)

Enunciado oficial de la actividad: [`docs/actividades/actividad_1_poo.md`](../actividades/actividad_1_poo.md). El entregable son **4 notebooks independientes, uno por pilar** (`abstraccion.ipynb`, `encapsulamiento.ipynb`, `herencia.ipynb`, `polimorfismo.ipynb`), cada uno con un ejemplo **propio del estudiante** — no las plantillas con `# TODO: completar` de `class_poo/ejercicios/`, que son solo material de práctica opcional y no se califican.

Corresponde a los 4 pilares cubiertos en `class_poo/`: `abstraccion.ipynb`, `encapsulamiento.ipynb`, `herencia.ipynb`, `polimorfismo.ipynb` (más `interfaz.ipynb` y `definiendo_clases.ipynb` como apoyo conceptual).

## Resumen de dimensiones

| Dimensión | Puntos máximos |
|---|---|
| 1. Abstracción | 10 |
| 2. Encapsulamiento | 10 |
| 3. Herencia | 10 |
| 4. Polimorfismo | 10 |
| 5. Calidad y claridad del código | 10 |
| **Total** | **50** |

## 1. Abstracción (10 pts) — evalúa `abstraccion.ipynb`

El mínimo exigido es **2 clases que modelan la misma entidad del mundo real en 2 contextos/problemas distintos**, cada una quedándose solo con lo relevante a su contexto (ver actividad). El descriptor de cada nivel evalúa qué tan bien se cumple ese contraste, no una abstracción genérica de una sola clase.

| Nivel | Puntos | Descriptor |
|---|---|---|
| Excelente | 9-10 | Dos clases distintas modelan la misma entidad en dos contextos/problemas distintos, cada una limitando sus atributos/métodos a lo relevante para *su* contexto (idealmente con clase abstracta/interfaz explícita, ej. `ABC`/`abstractmethod`), y el notebook deja explícito (en código o markdown) qué se omitió deliberadamente en cada una y por qué. |
| Bueno | 7-8 | Hay dos clases razonables para sus respectivos contextos, pero el contraste no se explica (no queda claro qué se decidió omitir ni por qué en cada una), o falta el mecanismo formal de clase abstracta/interfaz. |
| Aceptable | 5-6 | Solo hay una clase (falta el segundo contexto), o las dos clases son prácticamente idénticas — no hay una decisión real de "qué es relevante para este contexto y qué no". |
| Insuficiente | 0-4 | No hay clases, o el código es procedural con clases nominales que no encapsulan ningún concepto real. |

## 2. Encapsulamiento (10 pts) — evalúa `encapsulamiento.ipynb`

| Nivel | Puntos | Descriptor |
|---|---|---|
| Excelente | 9-10 | Atributos protegidos/privados (`_attr`/`__attr` o `property`) con una interfaz pública controlada (getters/setters o `@property`) que valida o restringe el acceso al estado interno. |
| Bueno | 7-8 | Usa convención de atributos privados (`_`/`__`) pero sin lógica de validación en el acceso, o expone algunos atributos innecesariamente. |
| Aceptable | 5-6 | Todos los atributos son públicos pero al menos la lógica de negocio vive dentro de métodos de la clase (no hay manipulación externa directa del estado). |
| Insuficiente | 0-4 | Atributos públicos manipulados libremente desde fuera de la clase, sin ninguna protección ni intención de ocultar estado. |

## 3. Herencia (10 pts) — evalúa `herencia.ipynb`

| Nivel | Puntos | Descriptor |
|---|---|---|
| Excelente | 9-10 | Jerarquía superclase/subclase coherente (relación "es-un" real, no forzada), las subclases reutilizan comportamiento del padre y solo sobrescriben lo que realmente difiere. |
| Bueno | 7-8 | Hay herencia funcional pero alguna subclase sobrescribe métodos completos sin reutilizar `super()`, duplicando lógica que pudo heredarse. |
| Aceptable | 5-6 | Herencia superficial: existe `class Hijo(Padre)` pero la relación "es-un" es forzada o no aporta reutilización real de comportamiento. |
| Insuficiente | 0-4 | No hay herencia, o se usa para forzar relaciones que no son "es-un" (mal uso conceptual). |

## 4. Polimorfismo (10 pts) — evalúa `polimorfismo.ipynb`

| Nivel | Puntos | Descriptor |
|---|---|---|
| Excelente | 9-10 | Distintas subclases implementan el mismo método (mismo nombre/firma) con comportamiento propio, y el código cliente las invoca de forma uniforme sin `if type(obj) == X` para decidir el comportamiento. |
| Bueno | 7-8 | Hay sobrescritura de métodos entre subclases, pero el código cliente todavía usa alguna verificación de tipo explícita en vez de confiar en el despacho polimórfico. |
| Aceptable | 5-6 | Métodos con el mismo nombre en clases distintas, pero sin relación de herencia/interfaz común que garantice intercambiabilidad real. |
| Insuficiente | 0-4 | No hay evidencia de polimorfismo, o se simula con `if/elif` sobre tipos en vez de sobrescritura de métodos. |

## 5. Calidad y claridad del código (10 pts) — evalúa los 4 notebooks

Se aplica la tabla de niveles a cada uno de los 4 notebooks por separado y la nota de esta dimensión es el **promedio de los 4** (redondeado al entero más cercano). Un notebook débil baja el promedio pero no hunde por sí solo la dimensión completa si los otros tres son sólidos.

| Nivel | Puntos | Descriptor (por notebook) |
|---|---|---|
| Excelente | 9-10 | Nombres descriptivos, funciones/métodos cortos y de responsabilidad clara, código ejecuta sin errores, incluye al menos un ejemplo de uso (`if __name__ == "__main__"` o celda de prueba). |
| Bueno | 7-8 | Código correcto y ejecutable, pero con nombres poco descriptivos o algún método demasiado largo. |
| Aceptable | 5-6 | Código ejecuta pero con errores menores no bloqueantes (warnings, casos borde no manejados) o desorganización notable. |
| Insuficiente | 0-4 | El código no ejecuta (`SyntaxError`/`NameError`/etc.) o no hay forma de verificar que funciona. |
