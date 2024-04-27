class Automovil {
    let ruedas: Int
    let puertdas: Int
    
    init() {
        self.ruedas = 4
        self.puertdas = 4
    }
    
    func velocidad(){
        print("voy a 50 km/h")
    }
}

class Mercedes : Automovil {
    let marca : String = "Mercedes"
    
    override func velocidad() {
        print("voy a 120 km/h")
    }
}

//MARK: Esta es la clase Padre
let automóvil = Automovil() // SI REMPLAZAMOS ESTO POR MERCEDES EN VEZ DE AUTO, NO ME DEBERIA LANZAR NINGUN PROBLEMA

//MARK: Esta es la clase Hijo
//let automóvil = Mercedes()
automóvil.velocidad()



