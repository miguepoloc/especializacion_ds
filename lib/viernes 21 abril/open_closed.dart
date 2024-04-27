// Sin el principio Open/Closed
// ignore_for_file: avoid_print

import 'package:flutter/widgets.dart';

class ReportGenerator {
  String generateReport(String type) {
    if (type == 'pdf') {
      return 'Generando informe en formato PDF...';
    } else if (type == 'excel') {
      return 'Generando informe en formato Excel...';
    }
    return 'Tipo de informe no soportado';
  }
}

// Con el principio Open/Closed
abstract class Report {
  String generateReport();
}

class PDFReport implements Report {
  @override
  String generateReport() {
    return 'Generando informe en formato PDF';
  }
}

class ExcelReport implements Report {
  @override
  String generateReport() {
    return 'Generando informe en formato Excel';
  }
}

String generateReport(Report report) {
    return report.generateReport();
  }

class OpenClosed extends StatelessWidget {
  final ReportGenerator reportGenerator = ReportGenerator();
  OpenClosed({super.key});

  @override
  Widget build(BuildContext context) {
    print('\nSin seguir el principio Open/Closed');
    print(reportGenerator.generateReport('pdf'));
    print(reportGenerator.generateReport('excel'));

    print('\nAplicando el principio Open/Closed');
    PDFReport pdfReport = PDFReport();
    ExcelReport excelReport = ExcelReport();
    print(generateReport(pdfReport));
    print(generateReport(excelReport));

    return Container();
  }
}
