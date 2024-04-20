<?php


require_once './Vehiculo.php';
require_once './Auto.php';

echo '<h1>Ejemplo encapsulamiento</h1>';

$vehiculo = new Vehiculo('Mazda', 2020);
echo "Marca: " .$vehiculo->getMarca(). "<br><br>";
/* echo "Modelo: ".$vehiculo->getModelo(). "<br>"; */

$auto = new Auto('Suzuki', 2021, 4);

echo "Marca: " .$auto->getMarca(). "<br>";
echo "Puertas: ".$auto->getPuertas(). "<br>";
echo "Modelo: ".$auto->getModelo(). "<br>";