
public class Mascota {

    private String nombre;
    private Integer edad;
    private String duenio;
    private String comidaFavorita;
    private String descripcion;

    public Mascota(String nombre, Integer edad, String duenio, String comidaFavorita) {
        this.nombre = nombre;
        this.edad = edad;
        this.duenio = duenio;
        this.comidaFavorita = comidaFavorita;
    }

    public void conocerNombre() {
        this.descripcion = String.format("El nombre es: %s", this.nombre);
        System.out.println(this.descripcion);
    }

    public void conocerEdad() {
        this.descripcion = String.format("La edad es: %s", this.edad);
        System.out.println(this.descripcion);
    }

    public void conocerDuenio() {
        this.descripcion = String.format("El nombre del dueño es: %s", this.duenio);

        System.out.println(this.descripcion);
    }

    public void conocerComidaFavorita() {
        this.descripcion = String.format("Su comida favorita es: %s", this.comidaFavorita);
        System.out.println(this.descripcion);
    }

    public static void main(String[] args) {
        // Crear una instancia de Mascota
        Mascota miMascota = new Mascota("Firulais", 5, "Juan", "Croquetas");
        // Llamar a los métodos de la clase
        miMascota.conocerNombre();
        miMascota.conocerEdad();
        miMascota.conocerDuenio();
        miMascota.conocerComidaFavorita();
    }
}
