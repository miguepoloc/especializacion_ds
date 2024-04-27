// ignore_for_file: avoid_print

import 'package:flutter/widgets.dart';

class Animal{
  void hacerSonido(){
    print("Función base: Haciendo sonido.");
  }
}

class Perro extends Animal {
  @override
  void hacerSonido() {
    print("Perro: Guau guau!");
  }
}

class Gato extends Animal {
  @override
  void hacerSonido() {
    print("Gato: Miau Miauuuu!");
  }
}

class Polimorfismo extends StatelessWidget{
  final Animal animal = Animal();
  final Animal perro = Perro();
  final Animal gato = Gato();

  Polimorfismo({super.key});
  
  @override
  Widget build(BuildContext context) {
     animal.hacerSonido();
     perro.hacerSonido();
     gato.hacerSonido();

     return Container();
  }}