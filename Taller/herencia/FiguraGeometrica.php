<?php

class FiguraGeometrica
{
  protected $color;
  protected $base;
  protected $altura;

  public function __construct($color, $base = null, $altura = null)
  {
    $this->color = $color;
    $this->base = $base;
    $this->altura = $altura;
  }

  public function getColor()
  {
    return $this->color;
  }

  public function calcularArea() {
    return $this->base * $this->altura;
  }

}




