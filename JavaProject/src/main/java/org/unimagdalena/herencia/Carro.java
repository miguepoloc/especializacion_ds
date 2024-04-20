package org.unimagdalena.herencia;

import lombok.Data;

@Data
public class Carro extends Vehiculo{

    private int numeroPasajeros;

    public Carro(String modelo, String marca, String color, String placa, int numeroPasajeros) {
        super(modelo, marca, color, placa);
        this.numeroPasajeros = numeroPasajeros;
    }

    public Carro(int numeroPasajeros) {
        this.numeroPasajeros = numeroPasajeros;
    }

    @Override
    public void conducir() {
        super.conducir();
        System.out.println("El carro está en marcha.");
    }
}