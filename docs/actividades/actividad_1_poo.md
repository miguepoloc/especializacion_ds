# Actividad 1 — Programación Orientada a Objetos (50 pts)

## Qué se hace

Elige un **problema o dominio propio** (no uno visto en clase — puede ser de tu área de interés: agro, salud, finanzas, videojuegos, lo que quieras) y modélalo con clases aplicando los 4 pilares de la POO:

- **Abstracción**: decide qué atributos/comportamientos son relevantes para tu problema y cuáles omites.
- **Encapsulamiento**: protege el estado interno de tus clases, exponiendo solo una interfaz pública controlada.
- **Herencia**: identifica al menos una relación real "es-un" en tu dominio y modélala con una jerarquía de clases (superclase + al menos 2 subclases).
- **Polimorfismo**: al menos un método debe comportarse distinto según la subclase, invocado de forma uniforme desde el código cliente (sin `if type(obj) == X`).

No es un ejercicio de completar código: el diseño (qué clases existen, cómo se relacionan, qué decide cada pilar) es tuyo.

## Mínimos exigidos

- Al menos **3 clases** en total.
- Al menos **1 superclase con 2 subclases** (herencia real, no forzada).
- Al menos **1 método polimórfico**: mismo nombre, comportamiento distinto por subclase, invocado sin verificar el tipo desde el código cliente.
- Al menos **1 atributo protegido/privado** con una interfaz pública controlada (encapsulamiento real, no todo público).

Entregas por debajo de estos mínimos se evalúan igual con la rúbrica, pero no pueden superar el nivel "Aceptable" en la(s) dimensión(es) afectada(s).

## Qué se entrega

1. Un notebook o script con tu código, ejecutado, con al menos un ejemplo de uso que demuestre los 4 pilares en acción.
2. Un **diagrama UML de clases** de tu diseño (puedes usar Graphviz o PlantUML, como viste en `class_uml/`).

Dentro de tu carpeta:

```
entregas/<tu_codigo_estudiante>/actividad_1_poo/
  poo.ipynb          # o el nombre que prefieras
  diagrama_clases.png (o .puml)
```

**Nota**: los notebooks de `class_poo/ejercicios/` (con TODO para completar) son material de **práctica opcional** para prepararte — no son el entregable de esta actividad.

## Cómo se entrega

1. Rama propia: `entrega/<tu_codigo>-actividad1-poo`.
2. Crea tu carpeta en `entregas/` con el notebook y el diagrama.
3. Pull Request con título `Actividad 1 - POO - <Tu Nombre>`.
4. Trabajo **individual**.

## Cuándo

Se entrega el **sábado del Fin de Semana 1** (el mismo día que se dicta la sesión de POO), antes de finalizar el día.

## Cómo se califica

Rúbrica completa: [`docs/rubricas/poo.md`](../rubricas/poo.md) — 4 dimensiones (un pilar cada una, 10 pts) + calidad de código (10 pts), con 4 niveles de desempeño por dimensión. Puede evaluarse con asistencia de IA usando esa rúbrica como criterio — ver [`docs/rubricas/README.md`](../rubricas/README.md) para el flujo.
