package srp;

import srp.refactored.Book;
import srp.refactored.BookFilePersistence;
import srp.refactored.Page;

import java.io.IOException;
import java.util.List;

public class MainGodExample {
    public static void main(String[] args) throws IOException {
        System.out.println("Principio de Responsabilidad Unica - SRP - God Example");

        BookFilePersistence bookFilePersistence = new BookFilePersistence();

        List<Page> pages = List.of(Page.builder().number(1).content("Primera Pagina").build(),
                Page.builder().number(2).content("Segunda Pagina").build(),
                Page.builder().number(3).content("Tercera Pagina").build());

        Book godLibrary = new Book("GodLibrary", "God", pages);

        System.out.println("Autor del libro: "+godLibrary.getAuthor());
        System.out.println("Titulo del libro: "+godLibrary.getTitle());
        System.out.println("Numero de paginas: "+godLibrary.getPages().size());
        System.out.println("Pagina Actual: "+godLibrary.getCurrentPage());
        System.out.println("Guardar el Libro");
        bookFilePersistence.save(godLibrary);
        System.out.println("Libro Guardado Satisfactoriamente ");
    }
}
