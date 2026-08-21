# Ejercicios de SOLID (versión para estudiante)

Estos notebooks son la versión de práctica de los notebooks de `solid/`
(`single_responsibility`, `open_closed`, `liskov`, `interface_segregation`,
`dependency_inversion`). Conservan las explicaciones y el ejemplo "incorrecto"
(el que viola el principio) tal como están en el original, pero el código del
**ejemplo correcto** — el que aplica el principio — está incompleto a
propósito.

## Cómo trabajar con ellos

1. Lee las celdas markdown de introducción y del "Ejemplo Correcto" para
   entender qué se va a construir.
2. Completa cada bloque marcado con `# TODO: completar`. El docstring de cada
   método te dice exactamente qué debe hacer; reemplaza el
   `raise NotImplementedError(...)` por tu implementación.
3. Ejecuta la celda de **verificación** que sigue (contiene `assert`). Si no
   hay errores, tu solución es correcta.
4. El bloque de "Ejemplo de Violación" de cada notebook se deja completo y
   marcado como "solo lectura": su función es mostrar, por contraste, cómo se
   ve el código cuando **no** se respeta el principio — no es algo que debas
   completar. En `liskov_ejercicio.ipynb`, ese bloque incluso lanza un error a
   propósito al ejecutarse: es el comportamiento esperado, es la demostración
   de la violación del principio.

## Si te atascas

Cada ejercicio tiene su versión resuelta con el mismo nombre (sin el sufijo
`_ejercicio`) en la carpeta padre `solid/`. Por ejemplo, si estás trabajando
en `open_closed_ejercicio.ipynb`, puedes consultar `../open_closed.ipynb`.
