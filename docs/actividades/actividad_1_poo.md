# Actividad 1 — Programación Orientada a Objetos (50 pts)

## Qué se hace

Vas a entregar **4 notebooks independientes, uno por cada pilar de la POO** — `abstraccion.ipynb`, `encapsulamiento.ipynb`, `herencia.ipynb`, `polimorfismo.ipynb` — **no un único notebook que mezcle los cuatro**. Cada notebook tiene su propio ejemplo, sus propias clases y su propio diagrama UML. Los ejemplos no tienen que ser del mismo dominio ni contarse como una sola historia: cada pilar se explica mejor con el ejemplo que mejor lo ilustra, y eso puede (y suele) cambiar de un notebook a otro.

- **`abstraccion.ipynb`**: modela **dos clases que representan la misma entidad del mundo real, pero en dos contextos/problemas distintos**, cada una quedándose solo con los atributos relevantes para *su* contexto. Ejemplo para ilustrar el patrón (no lo copies literal — inventa tu propia entidad): un `Avion` en un sistema de reservas de vuelos (capacidad, aerolínea, ruta) es una clase muy distinta a un `Avion` en un sistema de mantenimiento (horas de vuelo, motor, última revisión) — es el mismo objeto del mundo real, pero dos abstracciones distintas porque el problema que resuelve cada sistema es distinto. Lo que debe quedar demostrado: abstraer no es "copiar la realidad completa", es decidir qué importa *para el problema que estás resolviendo* — por eso ambas clases coexisten en el mismo notebook, para que el contraste sea explícito.
- **`encapsulamiento.ipynb`**: ejemplo propio (inventado por ti, cualquier dominio) con al menos una clase que protege su estado interno (atributos `_privados`) y expone una interfaz pública controlada (getters/setters o `@property` con validación).
- **`herencia.ipynb`**: ejemplo propio con una superclase y al menos 2 subclases que modelen una relación "es-un" real en tu dominio (no forzada).
- **`polimorfismo.ipynb`**: ejemplo propio con al menos un método que se comporte distinto según la subclase, invocado de forma uniforme desde el código cliente.

No es un ejercicio de completar código: el diseño de cada ejemplo (qué clases existen, qué atributos y métodos tienen, cómo se relacionan) es tuyo, no la plantilla vista en clase.

## Mínimos exigidos

Por notebook:

- **`abstraccion.ipynb`**: 2 clases que modelan la misma entidad en 2 contextos distintos, cada una exponiendo solo lo relevante a su propio contexto.
- **`encapsulamiento.ipynb`**: al menos 1 atributo protegido/privado con una interfaz pública controlada (encapsulamiento real, no todo público).
- **`herencia.ipynb`**: 1 superclase con al menos 2 subclases (herencia real, no forzada).
- **`polimorfismo.ipynb`**: 1 método polimórfico — mismo nombre, comportamiento distinto por subclase, invocado sin verificar el tipo desde el código cliente.

Cada notebook debe ejecutar sin errores e incluir al menos un ejemplo de uso que demuestre el pilar correspondiente en acción.

Entregas por debajo de estos mínimos se evalúan igual con la rúbrica, pero no pueden superar el nivel "Aceptable" en la dimensión afectada.

## Qué se entrega

1. **4 notebooks**, uno por pilar, cada uno ejecutado con al menos un ejemplo de uso.
2. **4 diagramas UML de clases**, uno por notebook — uno por cada ejemplo (puedes embeberlo como celda markdown con Graphviz/PlantUML, como viste en `class_poo/`, o como archivo aparte).

Dentro de tu carpeta:

```
entregas/<tu_nombre_estudiante>/actividad_1_poo/
  abstraccion.ipynb
  encapsulamiento.ipynb
  herencia.ipynb
  polimorfismo.ipynb
  diagramas/                       # si no los embebes en el notebook
    abstraccion.png (o .puml)
    encapsulamiento.png (o .puml)
    herencia.png (o .puml)
    polimorfismo.png (o .puml)
```

**Nota**: los notebooks de `class_poo/ejercicios/` (con TODO para completar) son material de **práctica opcional** para prepararte — no son el entregable de esta actividad. Tus 4 notebooks deben tener ejemplos propios, no las plantillas de clase completadas.

## Cómo se entrega

1. Rama propia: `entrega/<tu_nombre>-actividad1-poo`.
2. Crea tu carpeta en `entregas/` con los 4 notebooks y sus 4 diagramas.
3. Pull Request con título `Actividad 1 - POO - <Tu Nombre>`.
4. Trabajo **individual**.

## Cuándo

Se entrega el **sábado del Fin de Semana 1** (el mismo día que se dicta la sesión de POO), antes de finalizar el día.

## Cómo se califica

Rúbrica completa: [`docs/rubricas/poo.md`](../rubricas/poo.md) — 4 dimensiones (un pilar cada una, 10 pts) + calidad de código (10 pts), con 4 niveles de desempeño por dimensión. Puede evaluarse con asistencia de IA usando esa rúbrica como criterio — ver [`docs/rubricas/README.md`](../rubricas/README.md) para el flujo.
