#Ejercicio 97 Crear un  menu bancario para consultar saldo, depositar, retirar y salir

class Cuenta:
    def __init__(self):
        self.saldo = 0

    def consultar(self):
        print("Saldo actual:", self.saldo)

    def depositar(self, monto):
        self.saldo = self.saldo + monto 
        print("Deposito realizado")

    def retirar(self, monto):
        if monto <= self.saldo:
            self.saldo = self.saldo - monto
            print("Retiro realizado")
        else:
            print("Fondos Insuficientes waway")

cuenta = Cuenta()
opcion = 0
while opcion != 4:
    print("BANCO")
    print("1. Consultar saldo")
    print("2. Depositar")
    print("3. Retirar")
    print("4. Salir")
    opcion = int(input("Elige una opcion (1-4)"))

    match opcion:
        case 1:
            cuenta.consultar()
        case 2:
            monto =float(input("Ingresa el monto que deseas depositar: "))
            cuenta.depositar(monto)
        case 3:
            monto = float(input("Ingresa el monto a retirar: "))
        case 4:
            print("Saliendo del BANCO")
        case _:
            print("Opcion no valida ingresa una opcion entre (1-4)")