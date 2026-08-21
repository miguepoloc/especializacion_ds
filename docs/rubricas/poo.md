# Rúbrica — Actividad 1: Programación Orientada a Objetos (50 pts)

Enunciado oficial de la actividad: [`docs/actividades/actividad_1_poo.md`](../actividades/actividad_1_poo.md) — completar los 4 notebooks de `class_poo/ejercicios/`.

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

## 1. Abstracción (10 pts)

| Nivel | Puntos | Descriptor |
|---|---|---|
| Excelente | 9-10 | Modela una entidad del mundo real limitando el contexto a lo relevante (usa clase abstracta o interfaz explícita, ej. `ABC`/`abstractmethod` en Python), omitiendo deliberadamente detalles irrelevantes al problema. |
| Bueno | 7-8 | Hay una abstracción clara (clase que representa un concepto), pero sin mecanismo formal de clase abstracta/interfaz, o mezcla algún detalle irrelevante al contexto. |
| Aceptable | 5-6 | Existe una clase, pero es una traducción literal de datos sin verdadera decisión de "qué omitir" — se nota que no hubo reflexión sobre el nivel de abstracción. |
| Insuficiente | 0-4 | No hay clases, o el código es procedural con clases nominales que no encapsulan ningún concepto real. |

## 2. Encapsulamiento (10 pts)

| Nivel | Puntos | Descriptor |
|---|---|---|
| Excelente | 9-10 | Atributos protegidos/privados (`_attr`/`__attr` o `property`) con una interfaz pública controlada (getters/setters o `@property`) que valida o restringe el acceso al estado interno. |
| Bueno | 7-8 | Usa convención de atributos privados (`_`/`__`) pero sin lógica de validación en el acceso, o expone algunos atributos innecesariamente. |
| Aceptable | 5-6 | Todos los atributos son públicos pero al menos la lógica de negocio vive dentro de métodos de la clase (no hay manipulación externa directa del estado). |
| Insuficiente | 0-4 | Atributos públicos manipulados libremente desde fuera de la clase, sin ninguna protección ni intención de ocultar estado. |

## 3. Herencia (10 pts)

| Nivel | Puntos | Descriptor |
|---|---|---|
| Excelente | 9-10 | Jerarquía superclase/subclase coherente (relación "es-un" real, no forzada), las subclases reutilizan comportamiento del padre y solo sobrescriben lo que realmente difiere. |
| Bueno | 7-8 | Hay herencia funcional pero alguna subclase sobrescribe métodos completos sin reutilizar `super()`, duplicando lógica que pudo heredarse. |
| Aceptable | 5-6 | Herencia superficial: existe `class Hijo(Padre)` pero la relación "es-un" es forzada o no aporta reutilización real de comportamiento. |
| Insuficiente | 0-4 | No hay herencia, o se usa para forzar relaciones que no son "es-un" (mal uso conceptual). |

## 4. Polimorfismo (10 pts)

| Nivel | Puntos | Descriptor |
|---|---|---|
| Excelente | 9-10 | Distintas subclases implementan el mismo método (mismo nombre/firma) con comportamiento propio, y el código cliente las invoca de forma uniforme sin `if type(obj) == X` para decidir el comportamiento. |
| Bueno | 7-8 | Hay sobrescritura de métodos entre subclases, pero el código cliente todavía usa alguna verificación de tipo explícita en vez de confiar en el despacho polimórfico. |
| Aceptable | 5-6 | Métodos con el mismo nombre en clases distintas, pero sin relación de herencia/interfaz común que garantice intercambiabilidad real. |
| Insuficiente | 0-4 | No hay evidencia de polimorfismo, o se simula con `if/elif` sobre tipos en vez de sobrescritura de métodos. |

## 5. Calidad y claridad del código (10 pts)

| Nivel | Puntos | Descriptor |
|---|---|---|
| Excelente | 9-10 | Nombres descriptivos, funciones/métodos cortos y de responsabilidad clara, código ejecuta sin errores, incluye al menos un ejemplo de uso (`if __name__ == "__main__"` o celda de prueba). |
| Bueno | 7-8 | Código correcto y ejecutable, pero con nombres poco descriptivos o algún método demasiado largo. |
| Aceptable | 5-6 | Código ejecuta pero con errores menores no bloqueantes (warnings, casos borde no manejados) o desorganización notable. |
| Insuficiente | 0-4 | El código no ejecuta (`SyntaxError`/`NameError`/etc.) o no hay forma de verificar que funciona. |
