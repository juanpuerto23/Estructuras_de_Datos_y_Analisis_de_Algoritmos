class Pila:
    def __init__(self):
        self.items = []
    
    def apilar(self, item):
        self.items.append(item)
    
    def desapilar(self):
        return self.items.pop()
    
    def pila_vacia(self):
        return self.items == []

import random
m = int(input("Ingrese la N cantidad de libros: "))
libros = [] * m

for i in range(m):
    categoria_libro = input("Ingrese la categoria del libro (A,B,C): ")
    libros.append(categoria_libro)
    i =+ 1
print("La lista creada es: ",libros)

pila = Pila()

for i in range(m):
    if libros[0] != "A":
        pila.apilar(libros[1])
        i =+1

print("La lista creada es:", libros)
