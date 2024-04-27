package srp.refactored;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;

@AllArgsConstructor
@Data
@Builder
public class Page {
    private Integer number;
    private String content;
}