#Ejercicio 91 Crear calculador que permita realizar operaciones hasta seleccionar salir 

class Calculadora:
    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        return a / b

calculadora = Calculadora()
opcion = 0

while opcion != 5:
    print("Selecciona una operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    opcion = int(input("Ingrese su opción (1-5): "))

    if opcion >= 1 and opcion <= 4:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))

        match opcion:
            case 1:
                print("La suma es: ", calculadora.sumar(a, b))
            case 2:
                print("La resta es: ", calculadora.restar(a, b))
            case 3:
                print("La multiplicación es: ", calculadora.multiplicar(a, b))
            case 4:
                if b == 0:
                    print("No se puede dividir entre cero.")
                else:
                    print("La división es: ", calculadora.dividir(a, b))
    elif opcion == 5:
        print("Saliendo de la calculadora.")
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
