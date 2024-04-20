package com.example.arquitecturamvvm

// Ejercicio 1:

class BiciElectrica () {
    fun getVelocity() : String {
        return "20KM"
    }

    fun getBattery() : String {
        return "20KM"
    }
}

class Bici() {
    fun getVelocity() : String {
        return "10KM"
    }
}

// Ejercicio 2: implementacion de interfaces
interface Animal {
    fun roar(): String
}

class cat: Animal {
    override fun roar(): String {
        return "Miauu"
    }
}

class dog: Animal {
    override fun roar(): String {
        return "Guauu"
    }
}

// Ejercicio 3: herencia de clases
open class Samsung() {
    open fun getModel () : String {
        return "Samsung"
    }
}

class SamsungGalaxyS20() : Samsung() {

    override fun getModel(): String {
        return "Samsung Galaxy S20 PRO"
    }
}

class SamsungGalaxyS30() : Samsung() {

    override fun getModel(): String {
        return "Samsung Galaxy S30 PRO"
    }
}




