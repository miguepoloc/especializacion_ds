# Rúbrica — Actividad 4: Proyecto integrador (350 pts)

Enunciado de referencia: *"Realizar y sustentar una API o un frontend con el framework de preferencia donde se utilicen mínimo 5 Patrones de Diseño, explicando qué estaba mal en el código anterior y cómo lo solucionaron."*

El estudiante trae su propio código previo ("antes") y lo refactoriza aplicando al menos 5 patrones GoF ("después"), defendiéndolo en una sustentación oral de 10-15 min (individual o por equipo) con preguntas improvisadas del docente sobre decisiones de diseño.

## Resumen de dimensiones

| Dimensión | Puntos máximos |
|---|---|
| 1. Diagnóstico del código "antes" | 60 |
| 2. Aplicación de los 5 patrones (20 c/u) | 100 |
| 3. Justificación de cada patrón elegido (10 c/u) | 50 |
| 4. Calidad del código refactorizado | 60 |
| 5. Sustentación oral | 80 |
| **Total** | **350** |

## 1. Diagnóstico del código "antes" (60 pts)

| Nivel | Puntos | Descriptor |
|---|---|---|
| Excelente | 54-60 | Identifica ≥4 problemas concretos y distintos (code smells, violaciones SOLID específicas) citando archivo:línea del código original, no descripciones genéricas ("el código era desordenado"). |
| Bueno | 42-53 | Identifica 2-3 problemas concretos con ubicación citada, pero deja pasar otros problemas evidentes del mismo código. |
| Aceptable | 30-41 | Identifica problemas de forma genérica/superficial (sin citar ubicación exacta) o solo 1 problema concreto bien ubicado. |
| Insuficiente | 0-29 | No hay diagnóstico explícito, o los "problemas" descritos no corresponden realmente al código mostrado. |

## 2. Aplicación de cada patrón (20 pts × 5 = 100 pts)

Evaluar cada uno de los 5 patrones con esta misma tabla:

| Nivel | Puntos | Descriptor |
|---|---|---|
| Excelente | 18-20 | El patrón resuelve exactamente el problema diagnosticado en la dimensión 1 para esa zona del código; la estructura de clases cumple los roles correctos del patrón. |
| Bueno | 14-17 | El patrón está bien implementado estructuralmente, pero no se conecta claramente con un problema específico del diagnóstico (se aplicó "porque tocaba", no como solución dirigida). |
| Aceptable | 10-13 | Implementación parcial o con algún rol del patrón mal resuelto (ej. un Factory Method que sigue usando `if/elif` internamente). |
| Insuficiente | 0-9 | El patrón se menciona pero no está realmente implementado, o el código ni siquiera ejecuta en esa parte. |

## 3. Justificación de cada patrón elegido (10 pts × 5 = 50 pts)

Evaluar cada uno de los 5 patrones con esta misma tabla:

| Nivel | Puntos | Descriptor |
|---|---|---|
| Excelente | 9-10 | Explica por qué eligió ese patrón y no una alternativa razonable (ej. "elegí Strategy y no un `if/elif` porque necesito añadir nuevos algoritmos sin tocar la clase existente — cumple OCP"). |
| Bueno | 7-8 | Explica qué hace el patrón y por qué aplica aquí, pero sin comparar con alternativas. |
| Aceptable | 5-6 | Justificación genérica ("es un buen patrón para esto") sin conectar con las características concretas del problema. |
| Insuficiente | 0-4 | Sin justificación, o la justificación es incorrecta/no corresponde al patrón realmente usado. |

## 4. Calidad del código refactorizado (60 pts)

| Nivel | Puntos | Descriptor |
|---|---|---|
| Excelente | 54-60 | El código ejecuta sin errores, no introduce nuevas violaciones SOLID al resolver las anteriores, incluye al menos pruebas mínimas o un ejemplo de uso reproducible, y es legible (nombres, estructura). |
| Bueno | 42-53 | Ejecuta correctamente y es razonablemente legible, pero sin ninguna prueba/ejemplo reproducible, o introduce una violación SOLID menor en otra parte. |
| Aceptable | 30-41 | Ejecuta con advertencias o casos borde no manejados; la legibilidad es inconsistente entre módulos. |
| Insuficiente | 0-29 | El código no ejecuta, o el refactor introduce más problemas de diseño de los que resuelve. |

## 5. Sustentación oral (80 pts)

Formato: 10-15 min por estudiante/equipo, preguntas improvisadas del docente sobre decisiones de diseño (no limitarse a lo que el estudiante trae preparado).

| Nivel | Puntos | Descriptor |
|---|---|---|
| Excelente | 72-80 | Explica el código propio con dominio (no solo lee el README), responde con seguridad y correctamente a preguntas improvisadas sobre por qué se tomó cada decisión de diseño, y puede describir qué haría distinto con más tiempo. |
| Bueno | 56-71 | Explica bien lo preparado, pero titubea o da respuestas parcialmente incorrectas ante preguntas improvisadas fuera de lo ensayado. |
| Aceptable | 40-55 | Explica el "qué" (qué patrón usó) pero no el "por qué" con solidez; varias preguntas improvisadas quedan sin responder o con respuestas evasivas. |
| Insuficiente | 0-39 | No puede explicar decisiones de diseño más allá de leer el código/README en voz alta, o hay evidencia de que no comprende el código presentado (posible autoría no propia). |
