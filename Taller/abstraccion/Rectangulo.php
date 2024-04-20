<?php

class Rectangulo 
{
  protected $base;
  protected $altura;
  protected  $color;

  public function __construct($color, $base, $altura)
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