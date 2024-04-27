/**
 * You can edit, run, and share this code.
 * play.kotlinlang.org
 */

data class User(
    val id: Int,
    val name: String,
    val correo: String,
    val password: String
)

class RegisterUseCase() {

    operator fun invoke(user: User) {
        if(validate(user)) {
            println("User already exits")
        }else {
            println("User registered")
        }
    }

    // mala practica, tener una instancia de una base de datos en un caso de uso
    // y ejecutar sentencias.

    fun validate(user: User): Boolean {
        val database = Database()
        return database.query("select * from user where id = " + user.id)
    }

}

class Database() {
    fun query(s: String): Boolean {
        // codigo que va a buscar en una base de datos
        // encuentra que el usuario ya existe(retorna true)
        return true
    }
}


fun main() {
    var user = User(0, "pepe", "pepe@gmail.com", "pepe123")
    println(RegisterUseCase().invoke(user))
}