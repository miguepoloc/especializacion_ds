package org.unimagdalena.geometria;

import lombok.Builder;
import lombok.Data;
import org.unimagdalena.interfaces.FiguraGeometrica;

@Builder
@Data
public class Triangulo implements FiguraGeometrica {

    private double base;
    private double altura;
    private double areaTriangulo;

    @Override
    public double calcularArea() {
       return areaTriangulo = (base * altura)/2;
    }
}
