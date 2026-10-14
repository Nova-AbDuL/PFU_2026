#Ejercicio 89 Leer N numeros y determinar cuantos son positivos, negativos y cero

class Numeros:
    def __init__(self):
        self.n = n
        self.positivos = 0
        self.negativos = 0
        self.ceros = 0

    def leer(self):
        for i in range(self.n):
            numero = int(input("Ingresa un numero: "))
            if numero > 0:
                self.positivos = self.positivos + 1
            elif numero < 0:
                self.negativos = self.negativos + 1
            else:
                self.ceros = self.ceros + 1

    def mostrar(self):
        print("Ingresaste: ", self.positivos, "numeros positivos")
        print("Ingresaste: ", self.negativos, "numeros negativos")
        print("Ingresaste: ", self.ceros, "ceros")

n = int(input("Cuantos numeros vas a ingresar?: "))

inicio = Numeros()
inicio.leer()
inicio.mostrar()