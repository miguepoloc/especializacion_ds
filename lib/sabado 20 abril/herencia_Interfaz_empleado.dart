// ignore_for_file: avoid_print

import 'package:flutter/widgets.dart';

abstract class Empleado {
  double calcularSalario();
  void mostrarDetalles();
}

class EmpleadoAsalariado extends Empleado {
  String nombre;
  double salarioMensual;

  EmpleadoAsalariado(this.nombre, this.salarioMensual);

  @override
  double calcularSalario() {
    return salarioMensual;
  }

  @override
  void mostrarDetalles() {
    print("Nombre: $nombre");
    print("Salario: $salarioMensual");
  }

  void pagarImpuestos() {
    double impuesto = salarioMensual * 0.05;
    print("El empleado $nombre pagó \$${impuesto.toStringAsFixed(2)} de impuestos");
  }
}

class EmpleadoPorHoras extends Empleado {
  String nombre;
  double horasTrabajadas;
  double salarioPorHora;

  EmpleadoPorHoras(this.nombre, this.horasTrabajadas, this.salarioPorHora);

  @override
  double calcularSalario() {
    return horasTrabajadas * salarioPorHora;
  }

  @override
  void mostrarDetalles() {
    print("Nombre: $nombre");
    print("Horas Trabajadas: $horasTrabajadas");
    print("Salario Por Hora: $salarioPorHora");
  }
}

class Interfaz_Herencia extends StatelessWidget {
  final EmpleadoAsalariado empleado1 = EmpleadoAsalariado('Juan', 1500000);
  final EmpleadoPorHoras empleado2 = EmpleadoPorHoras('Pedro', 20, 10000);

  Interfaz_Herencia({super.key});

  @override
  Widget build(BuildContext context) {
    empleado1.mostrarDetalles();
    print('Salario total: \$${empleado1.calcularSalario().toStringAsFixed(2)}');
    empleado1.pagarImpuestos();

    print("\n");
    empleado2.mostrarDetalles();
    print('Salario total: \$${empleado2.calcularSalario().toStringAsFixed(2)}');
    
    return Container();
  }
}
