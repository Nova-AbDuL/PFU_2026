#Ejercicio 87 leer 10 numeros y determinar el mayor y menor

class Numeros:
    def __init__(self):
        self.mayor = 0
        self.menor = 0

    def leer(self):
        for i in range(10):
            numero = int(input("Ingresa un numero: "))
            if i == 0:
                self.mayor = numero
                self.menor = numero
            else:
                if numero > self.mayor:
                    self.mayor = numero
                if numero < self.menor:
                    self.menor = numero

    def mostrar(self):
        print("El numero mayor es:", self.mayor)
        print("El numero menor es:", self.menor)

inicio = Numeros()
inicio.leer()
inicio.mostrar()