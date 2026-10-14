#Ejercicio 96 Ingresar productos y precios hasta seleccionar Finalizar

class Compra:
    def __init__(self):
        self.total = 0

    def agregar(self, nombre, precio):
        self.total = self.total + precio
        print("Producto agregado:", nombre)

    def mostrar_total(self):
        print("Total de la compra:", self.total)

compra = Compra()
opcion = 0

while opcion != 2:
    print("1. Agregar producto")
    print("2. Finalizar compra")
    opcion = int(input("Seleccione una opción: "))

    match opcion:
        case 1:
            nombre = input("Ingrese el nombre del producto: ")
            precio = float(input("Ingrese el precio del producto: "))
            compra.agregar(nombre, precio)
        case 2:
            compra.mostrar_total()
        case _:
            print("Opción inválida. Intente nuevamente.")