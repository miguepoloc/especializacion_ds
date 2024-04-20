<?php

class Vehiculo {
  protected $marca;
  private $modelo;

  public function __construct($marca, $modelo) {
      $this->marca = $marca;
      $this->modelo = $modelo;
  }

  public function getMarca() {
      return $this->marca;
  }

  private function getModelo(){
    return $this->modelo;
  }
}