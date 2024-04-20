package org.unimagdalena.herencia;

import lombok.Data;

@Data
public class Moto extends Vehiculo{

    private int cilindraje;

    public Moto(String modelo, String marca, String color, String placa, int cilindraje) {
        super(modelo, marca, color, placa);
        this.cilindraje = cilindraje;
    }

    public Moto(int cilindraje) {
        this.cilindraje = cilindraje;
    }

    @Override
    public void conducir() {
        super.conducir();
        System.out.println("La moto está en marcha.");
    }
}
