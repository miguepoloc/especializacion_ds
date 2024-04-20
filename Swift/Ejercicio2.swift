//
//  Ejercicio2.swift
//  Solid
//
//  Created by Juan Bernier on 20/04/24.
//

import Foundation


//MARK: EJERCICIO 2 - Crear una interfaz y aplicarlo sobre un objeto

//Creamos los diferentes lugares donde se pueda instalar apps en el celular
enum Store : String{
    case appStore = "App Store"
    case playStore = "Play Store"
}

//Creamos la funcion que deba aplicar nuestra clase
protocol OSProtocol {
    func downloadFrom(store: Store)
}

//La clase la cual debemos aplicar
class CellPhone : OSProtocol{
    init(){
        downloadFrom(store: .appStore)
    }
    func downloadFrom(store: Store) {
        print("Descargando de la \(store.rawValue)...")
    }
}


let phone = CellPhone()
