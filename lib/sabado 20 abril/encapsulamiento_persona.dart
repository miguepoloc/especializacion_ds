import 'package:flutter/material.dart';

class Persona {
  String _nombre;
  int _edad;

  Persona(this._nombre, this._edad);

  String getNombre() {
    return _nombre;
  }

  void setNombre(String newName) {
    _nombre = newName;
  }

  int getEdad() {
    return _edad;
  }

  void setEdad(int newAge) {
    if (newAge > 0) {
      _edad = newAge;
    }
  }
}

class Encapsulamiento extends StatelessWidget {
  Encapsulamiento({super.key});
  
  var persona1 = Persona("Juanita", 25);

  @override
  Widget build(BuildContext context) {
    print("Nombre: ${persona1.getNombre()}");
    print("Edad: ${persona1.getEdad()}");

    persona1.setNombre("Juana");
    persona1.setEdad(26);

    print("Nombre: ${persona1.getNombre()}");
    print("Edad: ${persona1.getEdad()}");

    return Container();
  }}
