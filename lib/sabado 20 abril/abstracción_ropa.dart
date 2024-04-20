
import 'package:flutter/material.dart';

class Ropa {
  final String nombre;
  final String? categoria;
  final String color;
  final String? talla;
  final double? precio;
  final bool? limpia;
  final int? posturas;

  Ropa({
    required this.color,
    this.talla,
    required this.nombre,
    this.categoria,
    this.precio,
    this.limpia,
    this.posturas,
  });

  @override
  String toString() {
    String result = '\n\nnombre: $nombre ';
    result += '\ncolor: $color ';
    if (categoria != null) result += '\ncategoria: $categoria ';
    if (limpia != null) result += '\nlimpia: $limpia ';
    if (posturas != null) result += '\nposturas: $posturas ';
    if (talla != null) result += '\ntalla: $talla ';
    if (precio != null) result += '\nprecio: $precio';
    return result;
  }
}

class Abstraccion extends StatefulWidget {
  const Abstraccion({super.key});

  @override
  State<Abstraccion> createState() => _AbstraccionState();
}

class _AbstraccionState extends State<Abstraccion> {
  final List<Ropa> productos = [
    Ropa(
        categoria: "Blusas",
        nombre: "Blusa cielo con mangas",
        color: "Azul",
        talla: "s",
        precio: 25000),
    Ropa(
        categoria: "Pantalones",
        nombre: "Pantalon de tela",
        color: 'Negro',
        talla: 'M',
        precio: 40000),
  ];

  final List<Ropa> closet = [
    Ropa(
        nombre: "Blusa cielo con mangas",
        color: "Azul",
        limpia: true,
        posturas: 0,),
    Ropa(
        nombre: "Pantalon de tela", 
        color: 'Negro', 
        posturas: 1, 
        limpia: true),
  ];

  String imprimirVenta() {
    return (productos.toString());
  }

  String imprimirCloset() {
    return (closet.toString());
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        body: Padding(
          padding: const EdgeInsets.all(80.0),
          child: Row(
            children: [
              Column(
                children: [
                  const Text("ROPA EN VENTA"),
                  Text(imprimirVenta()),
                ],
              ),
              const SizedBox(
                width: 400,
              ),
              Column(
                children: [
                  const Text("ROPA EN CLOSET"),
                  Text(imprimirCloset()),
                ], 
              )
            ],
          ),
        ),
      ),
    );
  }
}
