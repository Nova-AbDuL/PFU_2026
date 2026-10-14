#Ejercicio 100 Crear un menu para factorial, tabla de multiplicar, paridad y cuadrado

class Operaciones:
    def factorial(self, n):
        resultado = 1
        for i in range(1, n + 1):
            resultado = resultado * i
        print("El factorial de", n, "es:", resultado)

    def tabla(self, n):
        for i in range(1, 11):
            print(n, "x", i, "=", n * i)

    def paridad(self, n):
        if n % 2 == 0:
            print(n, "es un número par")
        else:
            print(n, "es un número impar")

    def cuadrado(self, n):
        print("El cuadrado de", n, "es:", n ** 2)

operaciones = Operaciones()
opcion = 0
while opcion != 5:
    print("Menú de operaciones:")
    print("1. Factorial")
    print("2. Tabla de multiplicar")
    print("3. Paridad")
    print("4. Cuadrado")
    print("5. Salir")
    opcion = int(input("Selecciona una opción (1-5): "))

    match opcion:
        case 1:
            n = int(input("Ingresa un número para calcular su factorial: "))
            operaciones.factorial(n)
        case 2:
            n = int(input("Ingresa un número para mostrar su tabla de multiplicar: "))
            operaciones.tabla(n)
        case 3:
            n = int(input("Ingresa un número para verificar su paridad: "))
            operaciones.paridad(n)
        case 4:
            n = int(input("Ingresa un número para calcular su cuadrado: "))
            operaciones.cuadrado(n)
        case 5:
            print("Saliendo del programa")
        case _:
            print("Opción no válida, por favor selecciona una opción del 1 al 5")