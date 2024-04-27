package srp.refactored;

import lombok.AllArgsConstructor;
import lombok.Data;

@AllArgsConstructor
@Data
public class Page {
    private Integer number;
    private String content;
}