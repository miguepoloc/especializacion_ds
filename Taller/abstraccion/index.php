<?php
require_once './Rectangulo.php';
require_once './Circulo.php';


echo '<h1>Ejemplo de abstraccion</h1>';
$rectangulo = new Rectangulo("Rojo", 5, 10);
echo "Área del rectángulo: " . $rectangulo->calcularArea() .'<br>'; 
echo "Color del rectángulo: " . $rectangulo->getColor(); 

echo '<br><br>';
$circulo = new Circulo("Azul", 3);
echo "Área del círculo: " . $circulo->calcularArea() .'<br>';
echo "Color del círculo: " . $circulo->getColor();
