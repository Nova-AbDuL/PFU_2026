#Ejercicio 92 Crear un menu con figuras geometricas y permitir calcular areas repetidamente

class Figuras:
    def area_circulo(self, radio):
        return 3.14159 * radio ** 2

    def area_rectangulo(self, base, altura):
        return base * altura

    def area_triangulo(self, base, altura):
        return (base * altura) / 2

    def area_cuadrado(self, lado):
        return lado ** 2

figuras = Figuras()
opcion = 0

while opcion != 5:
    print("Selecciona una figura para calcular su área:")
    print("1. Círculo")
    print("2. Rectángulo")
    print("3. Triángulo")
    print("4. Cuadrado")
    print("5. Salir")
    opcion = int(input("Ingrese su opción (1-5): "))

    match opcion:
        case 1:
            radio = float(input("Ingrese el radio del círculo: "))
            print("El área del círculo es: ", figuras.area_circulo(radio))
        case 2:
            base = float(input("Ingrese la base del rectángulo: "))
            altura = float(input("Ingrese la altura del rectángulo: "))
            print("El área del rectángulo es: ", figuras.area_rectangulo(base, altura))
        case 3:
            base = float(input("Ingrese la base del triángulo: "))
            altura = float(input("Ingrese la altura del triángulo: "))
            print("El área del triángulo es: ", figuras.area_triangulo(base, altura))
        case 4:
            lado = float(input("Ingrese el lado del cuadrado: "))
            print("El área del cuadrado es: ", figuras.area_cuadrado(lado))
        case 5:
            print("Saliendo del programa.")
        case _:
            print("Opción inválida. Por favor, seleccione una opción válida.")