#Ejercicio 94 Registrar edades hasta ingresar 0 y determinar cantidad de mayores y menores

class Edades:
    def __init__(self):
        self.mayores = 0
        self.menores = 0

    def leer(self):
        edad = int(input("Ingrese la edad de la persona (o 0 para finalizar): "))
        while edad != 0:
            if edad >= 18:
                self.mayores = self.mayores + 1
            else:
                self.menores = self.menores + 1
            edad = int(input("Ingrese la edad de la persona (o 0 para finalizar): "))

    def mostrar(self):
        print("Cantidad de mayores de edad: ", self.mayores)
        print("Cantidad de menores de edad: ", self.menores)

inicio = Edades()
inicio.leer()
inicio.mostrar()