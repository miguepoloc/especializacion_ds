<?php
require_once './FiguraGeometrica.php';
class Rectangulo extends FiguraGeometrica
{
 

  public function __construct($color, $base, $altura)
  {
    parent::__construct($color, $base, $altura);
  }
}

