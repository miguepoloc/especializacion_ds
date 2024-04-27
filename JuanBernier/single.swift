import Cocoa

struct Book{
    let cover : String
}

//MALA PRACTICA
class UserAuthentication {
    var username: String
    var password: String
    var token: String
    
    init(username: String, password: String, token: String) {
        self.username = username
        self.password = password
        self.token = token
    }
    
    func register(){
        //login of registering a user here and saves information in the token
        username = "juan"
        password = "password"
        token = "123"
    }
    
    func fetchBooks(_ withToken : String) -> Book?{
        //fetches books information depending on user credentials
        if withToken != "" {
            return Book(cover: "Harry Potter")
        }
        return nil
    }
}






//BUENA PRACTICA
class UserAuthentication2 {
    var username: String
    var password: String
    var token: String
    
    init() {
        username = "juan"
        password = "password"
        token = ""
        register()
    }
    
    func register(){
        //login of registering a user here and saves information in the token
        token = "123"
    }
}

class FetchData {
    let token : String
    var book : Book?
    
    init(token: String) {
        self.token = token
    }
    
    func fetchBooks() -> Book?{
        //fetches books information depending on user credentials
        if token != "" {
            book = Book(cover: "Harry Potter")
        }
        return nil
    }
}


let user = UserAuthentication2()
let books = FetchData(token: user.token)
books.fetchBooks()
if let book = books.book {
    print(book)
}
