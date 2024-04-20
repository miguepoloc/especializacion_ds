<?php

class Auto extends Vehiculo {
  private $puertas;

  public function __construct($marca, $modelo, $puertas) {
      parent::__construct($marca, $modelo);
      $this->puertas = $puertas;
  }

  public function getPuertas() {
    return $this->puertas;
  }
}