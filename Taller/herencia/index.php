<?php
require_once './Rectangulo.php';
require_once './Triangulo.php';

echo '<h1>Ejemplo de herencia</h1>';

$rectangulo = new Rectangulo("Rojo", 5, 10);
echo "Área del rectángulo: " . $rectangulo->calcularArea() .'<br>'; 
echo "Color del rectángulo: " . $rectangulo->getColor(); 

echo '<br><br>';
$triangulo = new Triangulo("Verde", 8, 6);
echo "Área del triángulo: " . $triangulo->calcularArea() . '<br>';
echo "Color del triángulo: " . $triangulo->getColor();
