package srp;

import srp.badexample.Book;
import srp.badexample.Page;

import java.io.IOException;
import java.util.List;

public class MainBadExample {
    public static void main(String[] args) throws IOException {
        System.out.println("Principio de Responsabilidad Unica - SRP - Bad Example");

        List<Page> pages = List.of(Page.builder().number(1).content("Primera Pagina").build(),
                Page.builder().number(2).content("Segunda Pagina").build(),
                Page.builder().number(3).content("Tercera Pagina").build());

        Book badLibrary = new Book("BadLibrary", "Bad", pages);

        System.out.println("Autor del libro: "+badLibrary.getAuthor());
        System.out.println("Titulo del libro: "+badLibrary.getTitle());
        System.out.println("Numero de paginas: "+badLibrary.getPages().size());
        System.out.println("Pagina Actual: "+badLibrary.getCurrentPage());
        System.out.println("Guardar el Libro");
        badLibrary.save();
        System.out.println("Libro Guardado Satisfactoriamente ");
    }
}
