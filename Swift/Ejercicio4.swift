//
//  Ejercicio4.swift
//  Solid
//
//  Created by Juan Bernier on 20/04/24.
//

import Foundation


//MARK: Ejercicio 4 - Crear una clase con atributos privados y públicos

class Example {
    
    //atributo publico el cual se puede acceder
    let name: String
    //atributo privado y no se puede acceder a el directamente
    private var document : String = ""
    
    init(name: String) {
        self.name = name
        self.createDocument()
    }
    
    //metodo publico
    func hablar() {
        print("hola me llamo \(name)")
    }
    
    //método privado y no te permitirá visualizar esto
    private func createDocument(){
        document = "documentID: \(name)-123123123"
    }
}


let ejemplo = Example(name: "Alexandra")
//llama al metodo publico
ejemplo.hablar()
//falla al llamar metodo privado
//ejemplo.createDocument()
