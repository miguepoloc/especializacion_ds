# Ejercicios de POO (versión para estudiante)

Estos notebooks son la versión de práctica de los notebooks de `class_poo/`
(`abstraccion`, `encapsulamiento`, `herencia`, `polimorfismo`). Conservan las
explicaciones, diagramas UML y ejemplos de contexto originales, pero el
código de las clases está incompleto a propósito.

## Cómo trabajar con ellos

1. Lee las celdas markdown de cada ejemplo para entender qué se va a construir.
2. Completa cada bloque marcado con `# TODO: completar`. El docstring de cada
   método te dice exactamente qué debe hacer; reemplaza el
   `raise NotImplementedError(...)` por tu implementación.
3. Ejecuta la celda de **verificación** que sigue a cada clase (contiene
   `assert` o un comentario con la salida esperada). Si no hay errores, tu
   solución es correcta.
4. Algunos ejemplos (por ejemplo, en `herencia_ejercicio.ipynb`: el error de
   olvidar `super().__init__()` y el orden de resolución de métodos — MRO) se
   dejan completos y marcados como "solo lectura", porque su objetivo es
   ilustrar un comportamiento o un error común, no algo que debas escribir.

## Si te atascas

Cada ejercicio tiene su versión resuelta con el mismo nombre (sin el sufijo
`_ejercicio`) en la carpeta padre `class_poo/`. Por ejemplo, si estás
trabajando en `herencia_ejercicio.ipynb`, puedes consultar `../herencia.ipynb`.
