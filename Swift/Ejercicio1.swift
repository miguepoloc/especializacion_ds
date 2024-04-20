//
//  main.swift
//  Solid
//
//  Created by Juan Bernier on 20/04/24.
//

import Foundation

//MARK: EJERCICIO 1 - Crear dos clases similares que tengan cosas en comun

enum Browser{
    case chrome
    case safari
}

//clase 1
class Android {
    let navigator: Browser
    init() {
        self.navigator = .chrome
    }
}

//clase 2
class IOS {
    let navigator: Browser
    init() {
        self.navigator = .safari
    }
}

