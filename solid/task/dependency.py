#In this case we not use 'Dependency inversion Principle'

class PDFGenerator:
    def generate(self, data) -> str:
        # Lógica para generar un informe en PDF
        return "PDF report generated successfully"

class CSVGenerator:
    def generate(self, data) -> str:
        return "CSV report generated successfully"

#Acá el problema es que report depende de los generadores, entonces si queremos
#añadir más formatos para generar reportes, rompemos report que es más alto nivel
#que los generadores de formato. Es decir, es más importante hacer el reporte
# y no podemos detener la generación del reporte porque una herramienta no funciona

class Report:
    def __init__(self, format) -> None:
        self.format = format

    def generate_report(self, data) -> str:
        if self.format == 'PDF':
            generator = PDFGenerator()
        elif self.format == 'CSV':
            generator = CSVGenerator()
        else:
            raise ValueError("Unsupported format")
        return generator.generate(data)



# pdf_report = Report('PDF')
# print(pdf_report.generate_report('Datos del documento'))

# csv_report = Report('CSV')
# print(pdf_report.generate_report('Datos del documento'))

#In this case we use 'Dependency Inversion Principle'

from abc import ABC, abstractmethod
#Acá cambiamos la cosa. Ahora tenemos una interfaz que crea un reporte con un
#método que luego tendrá un polimorfismo por las clases generadoras de documentos

class ReportGenerator(ABC):
    @abstractmethod
    def generate(self, data):
        pass

class PDFGenerator(ReportGenerator):
    def generate(self, data) -> str:
        return "PDF report generated successfully"

class CSVGenerator(ReportGenerator):
    def generate(self, data) -> str:
        return "CSV report generated successfully"


#Ahora la clase report solo recibe una instancia de la interfaz generadora, pero
#esta instancia ya en sí misma define el formato del reporte y solo es utilizada
#para darle formato al reporte, porque el reporte no necesita los detalles de este
class Report:
    def __init__(self, generator) -> None:
        self.generator = generator

    def generate_report(self, data) -> str:
        return self.generator.generate(data)


pdf_generator = PDFGenerator()
pdf_report = Report(pdf_generator)
print(pdf_report.generate_report(data='Información del documento'))

csv_generator = CSVGenerator()
csv_report = Report(csv_generator)
print(csv_report.generate_report(data="Información del documento"))
