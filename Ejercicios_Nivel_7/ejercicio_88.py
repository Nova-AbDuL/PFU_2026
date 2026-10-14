#Ejercicio 88 leer N numeros y calcular suma y promedio

class Numeros:
    def __init__(self):
        self.n = n
        self.suma = 0

    def leer(self):
        for i in range(self.n):
            numero = float(input("Ingresa el número: "))
            self.suma = self.suma + numero

    def mostrar(self):
        promedio = self.suma / self.n
        print ("La suma de los números ingresaados es:", self.suma)
        print ("El promedio de los números ingresados es:", promedio)

n = int(input("Ingrese la cantidad de números que desea ingresar: "))
inicio = Numeros()
inicio.leer()
inicio.mostrar()