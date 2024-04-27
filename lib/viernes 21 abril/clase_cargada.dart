// ignore_for_file: avoid_print, prefer_interpolation_to_compose_strings

import 'package:flutter/widgets.dart';

class Car {
  final String color;
  final String brand;
  final int year;
  final double basePrice;

  Car({required this.color, required this.brand, required this.year, required this.basePrice});

  double calculatePrice() {
    double taxes = basePrice * 0.1;
    int yearsOld = DateTime.now().year - year;
    double depreciation = basePrice * 0.01 * yearsOld;

    return basePrice + taxes - depreciation;
  }

  @override
  String toString() {
    return 'Carro{color: $color, marca: $brand, año: $year}';
  }
}

class ClaseCargada extends StatelessWidget{
  
  final Car carro1 = Car (color: 'azul', brand: 'Toyota', year: 2020, basePrice: 5000000);

  ClaseCargada({super.key});
  @override
  Widget build(BuildContext context) {
    print("CARRO 1: "+ carro1.toString());
    print("PRECIO CARRO 1: "+ carro1.calculatePrice().toString());

    return Container();
  }
}