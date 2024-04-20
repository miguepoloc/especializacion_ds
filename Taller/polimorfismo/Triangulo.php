<?php
require_once './FiguraGeometrica.php';
class Triangulo extends FiguraGeometrica
{
  protected $base;
  protected $altura;

  public function __construct($color, $base, $altura)
  {
    parent::__construct($color, $base, $altura);
  }
}


