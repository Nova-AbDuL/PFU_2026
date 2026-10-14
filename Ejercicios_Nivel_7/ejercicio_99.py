#Ejericicio 99 Leer N edades y determinar cuantas correspondes a niños, adolecentes, adultos y adultos mayores

class Edades:
    def __init__(self, n):
        self.n = n
        self.ninos = 0
        self.adolescentes = 0
        self.adultos = 0
        self.adultos_mayores = 0
    
    def leer(self):
        for i in range(self.n):
            edad = int(input("Ingresa la edad: "))
            while edad < 1 or edad > 98:
                print("La edad debe estar entre 1 y 98")
                edad = int(input("Ingresa la edad: "))
            if edad<= 11:
                self.ninos = self.ninos + 1
            elif edad <=17:
                self.adolescentes = self.adolescentes + 1
            elif edad <= 59:
                self.adultos = self.adultos + 1
            else:
                self.adultos_mayores = self.adultos_mayores + 1

    def mostrar(self):
        print("Cantidad de niños: ", self.ninos)
        print("Cantidad de adolescentes: ", self.adolescentes)
        print("Cantidad de adultos: ", self.adultos)
        print("Cantidad de adultos mayores: ", self.adultos_mayores)

n = int(input("Ingresa la cantidad de edades que vas a ingresar: "))
inicio = Edades(n)
inicio.leer()
inicio.mostrar()