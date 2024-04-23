class CuentaB():
    def __init__(self, nombre: str, typeCuenta: str, saldo: int, ID: int) -> None:
        self.Nombre = nombre
        self.Type_cuenta = typeCuenta
        self.Saldo = saldo
        self.N_Cuenta = ID    

    def consultarSaldo(self) -> None:
        print(f"Saldo: {self.Saldo}")

    def ValidarOperacion(self, monto) -> None:
        if(monto>=self.Saldo): return(True); return(False)
    
    def Transferencia(self, monto: int, OtraCuenta) -> None:
        if self.ValidarOperacion(monto): 
            OtraCuenta.saldo += monto
            self.Saldo -= monto;
            print ("Sin saldo")

    def Transferencia(self, monto: int, OtraCuenta) -> None:
        if self.ValidarOperacion(monto): 
            OtraCuenta.saldo += monto
            self.Saldo -= monto
            print("Sin saldo")

##---------------------------------------------------------------------------------------------

class CuentaC():
    def __init__(self, nombre: str, typeCuenta: str, saldo: int, ID: int) -> None:
        self.Nombre = nombre
        self.Type_cuenta = typeCuenta
        self.Saldo = saldo
        self.id = ID

    def consultarSaldo(self) -> None:
        print(f"Saldo: {self.Saldo}")

    def ValidarOperacion(self, monto) -> None:
        if(monto>=self.Saldo): return(True); return(False)
    
    def MovimientoSalida(self, monto: int, OtraCuenta) -> None:
        
        if self.ValidarOperacion(monto): 
            OtraCuenta.saldo += monto
            self.Saldo -= monto
            print("Sin saldo")