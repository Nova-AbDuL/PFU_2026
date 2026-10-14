#Ejercicio 90 Mostrar la tabla de multiplicar de un numero y permite repetir el proceso para diferentes numeros

class tabla:
    def __init__(self, numero):
        self.numero = numero

    def mostrar(self):
        for i in range(1, 11):
            print(self.numero, "x", i, "=", self.numero * i)

respuesta = "s"
while respuesta =="s":
    numero = int(input("Ingresa un numero para mostrar su tabla de multiplicar: "))
    inicio = tabla(numero)
    inicio.mostrar()
    respuesta = input("Quieres ver otra tabla wacho? (s/n): ")