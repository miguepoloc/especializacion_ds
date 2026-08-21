# Python de 0 a experto

Material de práctica de la **sesión 2** del curso (FDS 1, sábado —
entre el calentamiento de UML y el inicio de Programación Orientada a
Objetos). Acompaña al deck `sesiones/02_Python.pptx`.

El público de este módulo ya sabe programar en algún otro lenguaje, así
que los notebooks van directo a la sintaxis y semántica específica de
Python (no explican qué es una variable o un condicional en general).

## Notebooks, en orden sugerido de estudio

1. **`01_sintaxis_y_tipos.ipynb`** — indentación significativa, tipado
   dinámico (pero fuerte), tipos primitivos, operadores, control de flujo
   (`if`/`for`/`while`).
2. **`02_estructuras_de_datos.ipynb`** — listas, tuplas, diccionarios y
   sets: creación, métodos comunes y cuándo usar cada una.
3. **`03_funciones.ipynb`** — parámetros por defecto, `*args`, `**kwargs`,
   desempaquetado y funciones como objetos de primera clase.
4. **`04_comprehensions_y_excepciones.ipynb`** — list/dict/set
   comprehensions y manejo de errores con `try/except/finally` +
   excepciones propias.
5. **`05_modulos_y_archivos.ipynb`** — formas de `import`, cómo importar
   un módulo propio (`utilidades.py`, incluido en esta carpeta) y lectura/
   escritura de archivos con `with open(...)`.
6. **`06_type_hints_dataclasses_decoradores.ipynb`** — anotaciones de tipo
   (`typing`), `@dataclass` vs. clase normal, y decoradores (propios y los
   ya conocidos `@staticmethod`/`@property`).
7. **`07_pydantic.ipynb`** — `BaseModel`, validación automática y por qué
   es un ejemplo real de buen diseño con validación declarativa (conecta
   directamente con SOLID y Patrones de Diseño, más adelante en el curso).

`utilidades.py` es un módulo de apoyo (no un notebook) usado como ejemplo
de import propio en el notebook 5 — no lo elimines.

## Cómo usarlo

Igual que los notebooks de `class_poo/`, `solid/`, `patrones/` y
`refactoring/`: ábrelo en Jupyter (kernel del `.venv` del repo) y ejecuta
las celdas en orden. Cada notebook es independiente — puedes saltar
directamente al tema que necesites repasar, aunque el orden 1→7 sigue la
progresión básico → intermedio → avanzado del deck de la sesión.

## Dependencias

Requiere `pydantic` (usado solo en `07_pydantic.ipynb`), incluido en
`requirements.txt` del repo junto con el resto de dependencias del curso.
