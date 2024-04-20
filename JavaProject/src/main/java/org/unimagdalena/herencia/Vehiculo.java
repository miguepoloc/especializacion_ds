package org.unimagdalena.herencia;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

@Builder
@Data
@AllArgsConstructor
@NoArgsConstructor
public class Vehiculo {

    private String modelo;
    private String marca;
    private String color;
    private String placa;

    public void conducir(){
        System.out.println("El " + marca + " " + modelo + " está en movimiento.");
    }

}
