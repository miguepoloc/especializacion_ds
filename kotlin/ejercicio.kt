package com.example.arquitecturamvvm

// Ejercicio 1:

class BiciElectrica () {
    fun getVelocity() : String {
        return "20KM"
    }

    fun getBattery() : String {
        return "20V"
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

class Cat: Animal {
    override fun roar(): String {
        return "Miauu"
    }
}

class Dog: Animal {
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

// Ejercicio 4: encapsulamiento

class Example(private val name: String) {

    private var document: String = ""

    init {
        createDocument()
    }

    fun hablar() {
        println("hola me llamo $name")
    }

    private fun createDocument() {
        document = "documentID: $name-123123123"
    }
}

fun main() {
    // ejercicio 2:
    println(Cat().roar())
    println(Dog().roar())

    // ejercicio 3:
    println(SamsungGalaxyS20().getModel())
    println(SamsungGalaxyS30().getModel())

    // Ejercicio 4
    val ejemplo = Example("Alexandra")
    ejemplo.hablar()
    // No se puede llamar al método privado createDocument() desde fuera de la clase en Kotlin
}
