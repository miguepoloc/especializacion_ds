package org.unimagdalena.abstraccion;

import lombok.Builder;
import lombok.Data;

import java.time.LocalDate;

@Builder
@Data
public class Credito2 {

    private String nombreCliente;
    private LocalDate fechaPago;
    private Double intereses;
    private Double valorCuota;

}
