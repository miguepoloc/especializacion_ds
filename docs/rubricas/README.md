# Rúbricas de evaluación — Especialización POO / SOLID / Patrones de Diseño

Este directorio contiene las rúbricas analíticas de las 4 actividades del curso, diseñadas para dos usos simultáneos:

1. **Evaluación humana** — tablas legibles con niveles de desempeño y puntaje.
2. **Evaluación asistida por IA** — el mismo Markdown se puede pegar directamente en un prompt junto con el código del estudiante para obtener una propuesta de calificación con justificación por criterio, que el docente revisa y confirma antes de publicar la nota.

| Actividad | Archivo | Puntos |
|---|---|---|
| 1. POO | [poo.md](poo.md) | 50 |
| 2. SOLID | [solid.md](solid.md) | 50 |
| 3. Patrones de Diseño | [patrones.md](patrones.md) | 50 |
| 4. Proyecto integrador (refactor + 5 patrones + sustentación) | [proyecto.md](proyecto.md) | 350 |
| **Total** | | **500** |

Todas comparten el mismo formato: por cada dimensión, 4 niveles de desempeño (**Excelente / Bueno / Aceptable / Insuficiente**) con un rango de puntos y un descriptor concreto de qué debe observarse en el código para asignar ese nivel.

## Flujo de evaluación con IA (propuesta, no automática)

1. Reúne el código del estudiante (PR de GitHub) y la rúbrica correspondiente.
2. Usa un prompt como el siguiente (ajusta `{{RUBRICA}}` y `{{nombre}}`):

   > Eres un evaluador docente. Aplica ESTRICTAMENTE la siguiente rúbrica al código del estudiante. Para cada dimensión, cita el archivo y la línea concreta que sustenta el nivel asignado — si no hay evidencia en el código para un nivel alto, no lo asignes aunque el código "se vea bien" en general. Si un archivo no ejecuta o falta, la(s) dimensión(es) afectada(s) van en Insuficiente. Devuelve: por cada dimensión, nivel asignado + puntos + justificación citando archivo:línea; y al final, el puntaje total sumado.
   >
   > RÚBRICA:
   > {{RUBRICA}}
   >
   > CÓDIGO DEL ESTUDIANTE:
   > {{nombre}}

3. La IA devuelve una propuesta de calificación con evidencia citada — **el docente revisa y ajusta antes de publicar la nota**, no se publica el resultado de la IA sin revisión (ver decisión "IA propone, tú confirmas").
4. Guarda la justificación de la IA como respaldo ante posibles reclamos de nota — es más defendible que una nota sin desglose.

## Nota sobre el peso de "Sustentación" (Actividad 4)

Es el criterio de mayor peso relativo del curso (80/350 ≈ 23% del proyecto, ~16% de la nota total) y el más difícil de delegar a una IA por ser oral y en vivo — la rúbrica en [proyecto.md](proyecto.md) da descriptores concretos para que la calificación de la sustentación sea igual de trazable que el resto, aunque la apliques tú mismo en el momento en lugar de una IA.
