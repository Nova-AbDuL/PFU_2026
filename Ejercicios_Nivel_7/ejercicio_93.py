#Ejercicio 93 Solicitar notas de estudiantes hasta finalizar y calcular promedio mayor y menor

class Notas:
    def __init__(self):
        self.suma = 0
        self.cantidad = 0
        self.mayor = 0
        self.menor = 0

    def leer(self):
        nota = float(input("Ingrese la nota del estudiante (o -1 para finalizar): "))
        while nota != -1:
            if self.cantidad == 0:
                self.mayor = nota
                self.menor = nota
            else:
                if nota > self.mayor:
                    self.mayor = nota
                if nota < self.menor:
                    self.menor = nota
            self.suma = self.suma + nota
            self.cantidad = self.cantidad + 1
            nota = float(input("Ingrese la nota del estudiante (o -1 para finalizar): "))

    def mostrar(self):
        if self.cantidad > 0:
            print("Promedio de notas: ", self.suma / self.cantidad)
            print("Nota mayor: ", self.mayor)
            print("Nota menor: ", self.menor)
        else:
            print("No se ingresaron notas.")

inicio = Notas()
inicio.leer()
inicio.mostrar()