package org.unimagdalena.geometria;

import lombok.Builder;
import lombok.Data;
import org.unimagdalena.interfaces.FiguraGeometrica;

@Builder
@Data
public class Cuadrado implements FiguraGeometrica {

    private int lado;
    private int areaCuadrado;

    @Override
    public double calcularArea() {
        return areaCuadrado = lado * lado;
    }
}
