// ignore_for_file: avoid_print

// ------------------------- IMPLEMENTANDO INCORRECTAMENTE LISKOV ----------------------------------
import 'package:flutter/widgets.dart';

class Dispositivo {
  String nombre;
  bool encendido;

  Dispositivo(this.nombre, this.encendido);

  void encender() {
    encendido = true;
    print('Dispositivo encendido');
  }

  void apagar() {
    encendido = false;
    print('Dispositivo apagado');
  }
}

class Televisor implements Dispositivo {
  String marca;
  double pulgadas;
  @override
  String nombre;
  @override
  bool encendido;

  Televisor(this.nombre, this.encendido, this.marca, this.pulgadas);

  void encender() {
    print('$nombre: TV encendido'); // Comportamiento diferente
  }

  void apagar() {
    print('$nombre: TV apagado, Hasta luego.'); // Comportamiento diferente
  }

  void cambiarCanal(int canal) {
    print('$nombre cambiando al canal $canal');
  }
}

class Smartphone implements Dispositivo {
  String sistemaOperativo;
  String modelo;

  @override
  String nombre;
  @override
  bool encendido;

  Smartphone(this.nombre, this.encendido, this.sistemaOperativo, this.modelo);

  void encender() {
    print('$nombre: Smartphone encendido, listo para usar.'); // Comportamiento diferente
  }

  void apagar() {
    print('$nombre: Smartphone apagado.'); // Comportamiento diferente
  }

  void llamar(int numero) {
    print('$nombre llamando al $numero');
  }
}

class Liskov extends StatelessWidget {
  final Dispositivo dispositivoBase = Dispositivo('Dispositivo Genérico', false);
  final Televisor televisor = Televisor('Televisor Samsung', false, 'Samsung', 55.0);
  final Smartphone smartphone = Smartphone('iPhone 12', true, 'iOS', 'iPhone 12 Pro');

  Liskov({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    print('\n IMPLEMENTACIÓN INCORRECTA DE LISKOV');
    print('Estado del dispositivo (clase base): ${dispositivoBase.encendido}');
    dispositivoBase.encender();
    print('Estado del dispositivo genérico: ${dispositivoBase.encendido}');
    
    print('\n');
    televisor.encender();
    televisor.cambiarCanal(5);
    televisor.apagar();

    print('\n');
    smartphone.encender();
    smartphone.llamar(123456789);
    smartphone.apagar();
    
    return Container();
  }
}


//   ------------------------------------- IMPLEMENTANDO CORRECTAMENTE LISKOV ---------------------------------
// class Dispositivo {
//   String nombre;
//   bool encendido;

//   Dispositivo(this.nombre, this.encendido);

//   void encender() {
//     encendido = true;
//     print('Dispositivo encendido');
//   }

//   void apagar() {
//     encendido = false;
//     print('Dispositivo apagado');
//   }
// }

// class Televisor implements Dispositivo {
//   String marca;
//   double pulgadas;
//   @override
//   String nombre;
//   @override
//   bool encendido;

//   Televisor(this.nombre, this.encendido, this.marca, this.pulgadas);

//   @override
//   void encender() {
//     print('$nombre: TV encendido');
//   }

//   @override
//   void apagar() {
//     print('$nombre: TV apagado, Hasta luego.');
//   }

//   void cambiarCanal(int canal) {
//     print('$nombre cambiando al canal $canal');
//   }
// }

// class Smartphone implements Dispositivo {
//   String sistemaOperativo;
//   String modelo;

//   @override
//   String nombre;
//   @override
//   bool encendido;

//   Smartphone(this.nombre, this.encendido, this.sistemaOperativo, this.modelo);

//   @override
//   void encender() {
//     print('$nombre: Smartphone encendido, listo para usar.');
//   }

//   @override
//   void apagar() {
//     print('$nombre: Smartphone apagado.');
//   }

//   void llamar(int numero) {
//     print('$nombre llamando al $numero');
//   }
// }

// class Liskov extends StatelessWidget{
//   final Dispositivo dispositivoBase = Dispositivo('Dispositivo Genérico', false);
//   final Televisor televisor = Televisor('Televisor Samsung', false, 'Samsung', 55.0);
//   final Smartphone smartphone = Smartphone('iPhone 12', true, 'iOS', 'iPhone 12 Pro');

//   Liskov({super.key});

  
//   @override
//   Widget build(BuildContext context) {
//     print('\n IMPLEMENTACIÓN CORRECTA DE LISKOV');
//     print('Estado del dispositivo (clase base): ${dispositivoBase.encendido}');
//     dispositivoBase.encender();
//     print('Estado del dispositivo genérico: ${dispositivoBase.encendido}');
    
//     print('\n');
//     televisor.encender();
//     televisor.cambiarCanal(5);
//     televisor.apagar();

//     print('\n');
//     smartphone.encender();
//     smartphone.llamar(123456789);
//     smartphone.apagar();
    
//     return Container();
//   }
// }
