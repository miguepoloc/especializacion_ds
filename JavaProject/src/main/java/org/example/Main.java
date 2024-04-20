package org.example;

import org.unimagdalena.abstraccion.Credito;
import org.unimagdalena.abstraccion.Credito2;
import org.unimagdalena.geometria.Cuadrado;
import org.unimagdalena.geometria.Triangulo;
import org.unimagdalena.herencia.Carro;
import org.unimagdalena.herencia.Moto;

import java.time.LocalDate;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {
        abstraccion();
        interfaces();
        herenciaAndPolimorfismo();
    }

    public static void abstraccion(){
        Credito creditoContextoCliente = Credito.builder().monto(200000).plazo(12).tasaInteresEA(25.7).build();
        Credito2 creditoContextoBancario = Credito2.builder()
                .nombreCliente("Cesar Maiguel")
                .fechaPago(LocalDate.now())
                .intereses(12500.12)
                .valorCuota(285360.0).build();

        System.out.println("EJEMPLO DE ABSTRACCION");

        System.out.println("Credito Contexto Cliente");
        System.out.println("Monto solicitado: "+creditoContextoCliente.getMonto());
        System.out.println("Plazo: "+creditoContextoCliente.getPlazo());
        System.out.println("Tasa de Interes EA: "+creditoContextoCliente.getTasaInteresEA());

        System.out.println("------------------------------------");

        System.out.println("Credito Contexto Bancario");
        System.out.println("Nombre del cliente: "+creditoContextoBancario.getNombreCliente());
        System.out.println("Fecha de pago: "+creditoContextoBancario.getFechaPago());
        System.out.println("Intereses: "+creditoContextoBancario.getIntereses());
        System.out.println("Valor de la cuota: "+creditoContextoBancario.getValorCuota());

        System.out.println("------------------------------------");
    }

    public static void interfaces(){
        System.out.println("EJEMPLO DE IMPLEMENTACION DE INTERFACES");

        Cuadrado cuadrado = Cuadrado.builder().lado(8).build();
        System.out.println("EL AREA DEL CUADRADO ES: "+ cuadrado.calcularArea());

        Triangulo triangulo = Triangulo.builder().base(12).altura(5).build();
        System.out.println("EL AREA DEL TRIANGULO ES: "+ triangulo.calcularArea());

        System.out.println("------------------------------------");
    }

    public static void herenciaAndPolimorfismo(){

        Carro carro = new Carro("2024", "Nissan", "Rojo", "HQK085", 4);
        Moto moto = new Moto("2024", "Yamaha", "Plateado", "NRG05B", 159);

        System.out.println("EJEMPLO DE HERENCIA Y POLIMORFISMO");

        carro.conducir();
        moto.conducir();

        System.out.println("------------------------------------");
    }
}