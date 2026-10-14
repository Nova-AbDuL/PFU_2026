#Ejercicio 95 Leer numeros hasta 0 y determinar pares, impares positivos y negativos

class Numeros:
    def __init__(self):
        self.pares = 0
        self.impares = 0
        self.positivos = 0
        self.negativos = 0

    def leer(self):
        numero = int(input("Ingrese un número (0 para terminar): "))
        while numero != 0:
            if numero % 2 == 0:
                self.pares = self.pares + 1
            else:
                self.impares = self.impares + 1

            if numero > 0:
                self.positivos = self.positivos + 1
            else:
                self.negativos = self.negativos + 1

            numero = int(input("Ingrese un número (0 para terminar): "))

    def mostrar(self):
        print("La cantidad de números pares son:", self.pares)
        print("La cantidad de números impares son:", self.impares)
        print("La cantidad de números positivos son :", self.positivos)
        print("La cantidad de números negativos son:", self.negativos)

inicio = Numeros()
inicio.leer()
inicio.mostrar()