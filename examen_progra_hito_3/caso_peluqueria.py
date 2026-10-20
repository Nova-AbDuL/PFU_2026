class Nodo:
    def __init__(self, codigo, descripcion):
        self.codigo = codigo
        self.descripcion = descripcion
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, codigo, descripcion):
        nuevo = Nodo(codigo, descripcion)
        # Si la lista está vacía, el nuevo nodo es la cabeza
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            # Se recorre hasta el último nodo y se enlaza el nuevo
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo

    def mostrar(self):
        actual = self.cabeza
        while actual is not None:
            print(actual.codigo, actual.descripcion)
            actual = actual.siguiente


class Pila:
    def __init__(self):
        self.items = []

    def apilar(self, elemento):
        # Se agrega el elemento a la cima (al final de la lista)
        self.items.append(elemento)

    def desapilar(self):
        # Si la pila está vacía no se puede sacar nada
        if len(self.items) == 0:
            print("La pila está vacía")
            return None
        # Devuelve y elimina el último elemento agregado
        return self.items.pop()


class Cola:
    def __init__(self):
        self.items = []

    def encolar(self, elemento):
        # Se agrega el elemento al final
        self.items.append(elemento)

    def desencolar(self):
        # Si la cola está vacía no se puede sacar nada
        if len(self.items) == 0:
            print("La cola está vacía")
            return None
        # Devuelve y elimina el primer elemento agregado
        return self.items.pop(0)

    # Reto individual: contar los turnos pendientes
    def contar_pendientes(self):
        return len(self.items)


#PRUEBAS

lista = ListaEnlazada()
pila = Pila()
cola = Cola()

# Datos de prueba
datos = [("T01", "Corte"), ("T02", "Tinte"), ("T03", "Peinado")]

for codigo, descripcion in datos:
    lista.agregar(codigo, descripcion)  # se registra en la lista enlazada
    cola.encolar(codigo)                # se encola la solicitud
    pila.apilar(codigo)                 # se apila para probar LIFO

print("Lista enlazada:")
lista.mostrar()

print("\nTurnos pendientes:", cola.contar_pendientes())

print("\nPrueba FIFO (cola):")
print(cola.desencolar())
print("Turnos pendientes:", cola.contar_pendientes())
print(cola.desencolar())
print(cola.desencolar())
print("Turnos pendientes:", cola.contar_pendientes())
cola.desencolar()  # prueba de cola vacía

print("\nPrueba LIFO (pila):")
print(pila.desapilar())
print(pila.desapilar())
print(pila.desapilar())
pila.desapilar()  # prueba de pila vacía
