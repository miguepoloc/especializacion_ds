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

class RegisterUseCase(val userRepository: UserRepository) {
    
    operator fun invoke(user: User) {
        if(userRepository.getUser(user)) {
            println("User already exits")
        }else {
            // codigo que registra un usuario
            println("User registered")
        }
    }
}

class UserRepository(val dataBase : Database) {
    fun getUser(user: User): Boolean {
        return dataBase.getUser(user)
    }
}


class Database() {
    private fun query(s: String): Boolean {
        // codigo que va a buscar en una base de datos
        // encuentra que el usuario ya existe(retorna true)
        return true
    }
    
    fun getUser(user: User): Boolean {
        return query("select * from user where id = " + user.id)
    }
}


fun main() {
    var user = User(0, "pepe", "pepe@gmail.com", "pepe123")
    val dataBase = DataBase()
    val userRepository = UserRepository(dataBase)
    val useCase = RegisterUseCase(userRepository)
    println(useCase.invoke(user))
}
