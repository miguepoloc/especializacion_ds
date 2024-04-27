
//MARK: /MALA PRACTICA OPEN CLOSED =================================

//PASAR DE ESTO....
class Humano1 {
    func caminar(){}
    func correr(){}
    func comer(){}
    func hablar(){}
    func SerMedallistaOlimpico(){}
    func isDownSindrom() {}
}

// A ESTO....
class Humano2 {
    func caminar(){}
    func correr(){}
    func comerPatatasFritas() {}// -> AQUI SE VIOLARIA EL CERRADO PARA SU MODIFICACION
    func hablar(){}
    func SerMedallistaOlimpico(){}
    func isDownSindrom() {}
}


//MARK: MALA PRACTICA OPEN CLOSED =================================
protocol SuperHumano {
    func SerMedallistaOlimpico()
}
protocol HumanoConDownSindrome {
    func isDownSindrom()
}

//clase basica de las acciones de un humano
class Humano3 {
    func caminar(){}
    func correr(){}
    func comer(){}
    func hablar(){}
}

//para casos de ser un atleta olímpico
extension Humano3 : SuperHumano{
    func SerMedallistaOlimpico(){}
}

extension Humano3 : HumanoConDownSindrome {
    func isDownSindrom() {}
    
}
