<?php
require_once './FiguraGeometrica.php';
class Circulo extends FiguraGeometrica {
  protected $radio;

  public function __construct($color, $radio) {
      parent::__construct($color);
      $this->radio = $radio;
  }

  public function calcularArea() {
      return pi() * $this->radio * $this->radio;
  }
}


