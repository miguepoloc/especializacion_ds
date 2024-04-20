<?php
class Circulo
{
  protected $color;
  protected $radio;

  public function __construct($color, $radio)
  {
    $this->color = $color;
    $this->radio = $radio;
  }

  public function calcularArea()
  {
    return pi() * $this->radio * $this->radio;
  }

  public function getColor()
  {
    return $this->color;
  }
}
