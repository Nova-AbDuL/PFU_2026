#Ejercicio 86 Leer 10 numeros y determinar cuantos don pares y cuantos son impares

def ingresar_numero():
    while True:
        try:
            numero = int(input("Ingrese un número: "))
            return numero
        except ValueError:
            print("Por favor, ingrese un número entero.")

class Numeros:
    def __init__(self):
        self.pares = 0
        self.impares = 0

    def leer(self):
        for i in range(10):
            numero = ingresar_numero()
            if numero % 2 == 0:
                self.pares = self.pares + 1
            else:
                self.impares = self.impares + 1

    def mostrar(self):
        print("Ingresaste:", self.pares,"numeros pares")
        print("Ingresaste:", self.impares,"numeros impares")

inicio = Numeros()
inicio.leer()
inicio.mostrar()
