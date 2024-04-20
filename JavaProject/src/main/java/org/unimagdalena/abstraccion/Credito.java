package org.unimagdalena.abstraccion;

import lombok.Builder;
import lombok.Data;

@Builder
@Data
public class Credito {

    private Integer monto;
    private Integer plazo;
    private Double tasaInteresEA;

}
