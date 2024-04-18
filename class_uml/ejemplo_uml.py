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
