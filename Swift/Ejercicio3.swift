//
//  Ejercicio3.swift
//  Solid
//
//  Created by Juan Bernier on 20/04/24.
//

import Foundation


//MARK: EJERCICIO 3 - Crear una clase abstracta y que dos elementos herede de estas

//
class Celular {
    func getModel(){
        print("Default model")
    }
}

class Xiomi : Celular {
    override init() {
        super.init()
        self.getModel()
    }
    override func getModel() {
        print("Xiomi")
    }
}

class IPhone15 : Celular{
    override init() {
        super.init()
        getModel()
    }
    override func getModel() {
        print("iPhone 15")
    }
}


let first = IPhone15()
let second = Xiomi()

