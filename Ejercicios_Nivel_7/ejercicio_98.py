#Ejercicio 98 Ingresar 10 notas, clasificar aprobadas/reprobadas y mostrar estdisticas

class Notas:
    def __init__(self):
        self.aprobadas = 0
        self.reprobadas = 0
        self.suma = 0
        self.mayor = 0
        self.menor = 0

    def leer (self):
        for i in range (10):
            nota = float(input("Ingresa tu nota: "))
            while nota < 0 or nota > 100:
                print("La nota debe estar entre 0 y 100")
                nota = float(input("Ingresa tu nota: "))

            if nota >= 51:
                self.aprobadas =self.aprobadas + 1
            else:
                self.reprobadas =self.reprobadas + 1

            if i == 0:
                self.mayor = nota
                self.menor = nota
            else:
                if nota > self.mayor:
                    self.mayor = nota
                if nota < self.menor:
                    self.menor = nota

            self.suma = self.suma + nota

    def mostrar(self):
        print("Tienes:", self.aprobadas, "notas aprobadas")
        print("Tienes:", self.reprobadas, "notas reprobadas")
        print("Tu promedio es:", self.suma/10)
        print("Tu nota mas alta es:", self.mayor)
        print("Tu nota mas baja es:", self.menor)

inicio = Notas()
inicio.leer()
inicio.mostrar()