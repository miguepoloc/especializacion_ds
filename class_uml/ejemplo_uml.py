class Course:
    # Este es un método de la clase 'Course'. Si este método cambia (por ejemplo, si cambia su nombre o se
    # añade algún parámetro requerido, etc.), el código de la clase 'Professor' se romperá.
    def get_knowledge(self) -> str:
        # Este método representa el conocimiento que un curso puede proporcionar.
        return "knowledge"

    # def get_knowledge(self, texto: str) -> str:
    #     return f"knowledge {texto}"


class Student:
    # Este es un método de la clase 'Student'. Si este método cambia, el código de la clase 'Professor' se romperá.
    def remember(self, knowledge: str) -> None:
        # Este método representa la capacidad de un estudiante para recordar el conocimiento.
        print(f"El estudiante ha recordado {knowledge}")


class Professor:
    def __init__(self, student: Student) -> None:
        # Esto es un campo de la clase. Aquí, 'student' es una instancia de la clase 'Student' y se asigna al
        # campo 'student' de la clase 'Professor'. La clase 'Student' no es sólo una dependencia,
        # sino también una asociación.
        self.student = student

    # Este es un método de la clase. 'course' es una instancia de la clase 'Course'. La clase 'Course' es una
    # dependencia para la clase 'Professor'.
    def teach(self, course: Course) -> None:
        # Aquí se utiliza una instancia de la clase 'Course' como parámetro del método 'teach'.
        self.student.remember(
            course.get_knowledge()
        )  # Aquí, el profesor está enseñando al estudiante a recordar el conocimiento del curso.


# Creación de las instancias de las clases
student = Student()
course = Course()
professor = Professor(student)

# El profesor enseña al estudiante
professor.teach(course)

"""
La clase Course tiene un método get_knowledge(). Si este método cambia (por ejemplo, si cambia su nombre o se añade
algún parámetro requerido, etc.), el código de la clase Professor se romperá. Esto se llama dependencia.

La clase Student tiene un método remember(). Si este método cambia, el código de la clase Professor se romperá.
Esto también es una dependencia.

En la clase Professor, el campo student siempre está accesible para cualquier método de Professor.
Por lo tanto, la clase Student no es sólo una dependencia, sino también una asociación.
"""


# ----------------------------------------------------------------------
# AGREGACIÓN: Equipo "tiene" Jugadores, pero un Jugador existe
# independientemente del Equipo (relación todo-parte débil).
# Se dibuja con un rombo VACÍO (◇) del lado del "todo" (Equipo).
# ----------------------------------------------------------------------
class Jugador:
    def __init__(self, nombre: str) -> None:
        self.nombre = nombre


class Equipo:
    def __init__(self, nombre: str) -> None:
        self.nombre = nombre
        # 'jugadores' es una lista de instancias de Jugador que YA EXISTÍAN
        # antes de ser fichadas por este equipo. Son la "parte" en la
        # relación todo-parte, pero no dependen del "todo" para existir.
        self.jugadores: list[Jugador] = []

    def fichar(self, jugador: Jugador) -> None:
        self.jugadores.append(jugador)

    def disolver(self) -> None:
        # Al disolver el equipo, los jugadores NO desaparecen: solo dejan
        # de estar en esta lista. Pueden fichar por otro equipo.
        self.jugadores = []


# ----------------------------------------------------------------------
# COMPOSICIÓN: Carro "tiene" un Motor, y ese Motor específico fue creado
# junto con ese Carro y no tiene sentido fuera de él (relación todo-parte
# fuerte). Se dibuja con un rombo LLENO (◆) del lado del "todo" (Carro).
# ----------------------------------------------------------------------
class Motor:
    def __init__(self, caballos_de_fuerza: int) -> None:
        self.caballos_de_fuerza = caballos_de_fuerza


class Carro:
    def __init__(self, modelo: str, caballos_de_fuerza: int) -> None:
        self.modelo = modelo
        # El Motor se crea AQUÍ DENTRO, como parte del propio Carro. Nadie
        # más tiene una referencia a esta instancia de Motor.
        self.motor = Motor(caballos_de_fuerza)

    def destruir(self) -> None:
        # Al destruir el carro, ESTE motor específico deja de existir con
        # él: nadie más lo estaba usando.
        self.motor = None


# ----------------------------------------------------------------------
# HERENCIA (generalización): Estudiante y Profesor SON-UN Persona. Ambas
# clases heredan los atributos y métodos comunes definidos en Persona y
# solo agregan/sobrescriben lo que las distingue.
# Se dibuja con una flecha continua y punta triangular vacía (--|>), que
# siempre apunta de la subclase hacia la superclase.
# ----------------------------------------------------------------------
class Persona:
    def __init__(self, nombre: str) -> None:
        self.nombre = nombre

    def saludar(self) -> str:
        return f"Hola, soy {self.nombre}"


class Estudiante(Persona):
    def remember(self, knowledge: str) -> None:
        print(f"{self.nombre} ha recordado {knowledge}")


class Profesor(Persona):
    def __init__(self, nombre: str, estudiante: Estudiante) -> None:
        # super().__init__() reutiliza el constructor de Persona en vez de
        # repetir 'self.nombre = nombre' aquí.
        super().__init__(nombre)
        self.estudiante = estudiante

    def teach(self, course: Course) -> None:
        self.estudiante.remember(course.get_knowledge())


# ----------------------------------------------------------------------
# REALIZACIÓN (implementación de interfaz): Estudiante y Profesor CUMPLEN
# el contrato de Notificable, pero cada una lo implementa a su manera.
# A diferencia de la herencia, aquí no se comparte código, solo la firma
# del método — por eso Notificable es una clase abstracta (ABC), no una
# clase con lógica propia.
# Se dibuja con una flecha punteada y punta triangular vacía (..|>).
# ----------------------------------------------------------------------
from abc import ABC, abstractmethod


class Notificable(ABC):
    @abstractmethod
    def notificar(self, mensaje: str) -> None: ...


class EstudianteNotificable(Estudiante, Notificable):
    def notificar(self, mensaje: str) -> None:
        print(f"[Estudiante {self.nombre}] {mensaje}")


class ProfesorNotificable(Profesor, Notificable):
    def notificar(self, mensaje: str) -> None:
        print(f"[Profesor {self.nombre}] {mensaje}")


if __name__ == "__main__":
    equipo = Equipo("Tiburones")
    jugador1 = Jugador("Ana")
    jugador2 = Jugador("Luis")
    equipo.fichar(jugador1)
    equipo.fichar(jugador2)
    print(f"{equipo.nombre} tiene a {[j.nombre for j in equipo.jugadores]}")
    equipo.disolver()
    print(f"Equipo disuelto. Ana sigue existiendo: {jugador1.nombre}")

    carro = Carro("Corolla", 140)
    print(f"{carro.modelo} tiene un motor de {carro.motor.caballos_de_fuerza} hp")
    carro.destruir()
    print(f"Carro destruido. ¿Sigue el motor accesible?: {carro.motor}")

    ana_estudiante = EstudianteNotificable("Ana")
    juan_profesor = ProfesorNotificable("Juan", ana_estudiante)
    print(ana_estudiante.saludar())  # heredado de Persona
    print(juan_profesor.saludar())  # heredado de Persona
    print("¿Estudiante es-un Persona?", isinstance(ana_estudiante, Persona))
    ana_estudiante.notificar("Tu tarea vence mañana")  # implementado de Notificable
    juan_profesor.notificar("Tienes una reunión a las 3pm")  # implementado de Notificable
