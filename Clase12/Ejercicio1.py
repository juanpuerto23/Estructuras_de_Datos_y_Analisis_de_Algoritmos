import random

class Pila:
    def __init__(self):
        self.items = []
    
    def apilar(self, item):
        self.items.append(item)
    
    def desapilar(self):
        return self.items.pop()
    
    def pila_vacia(self):
        return self.items == []

def generar_categoria():
    categoria = random.randint(0, 2)
    if categoria == 0:
        return "A"
    elif categoria == 1:
        return "B"
    else:
        return "C"

def main():
    libros = Pila()
    n = 0

    while n < 3:
        n = int(input("Ingrese la cantidad de libros a generar (mayor o igual a 3): "))
        if n < 3:
            print("La cantidad de libros debe ser al menos 3. Intente nuevamente.")

    while True:
        libros = Pila()
        for _ in range(n):
            categoria = generar_categoria()
            libros.apilar(categoria)

        if libros.items[0] == "A" and libros.items[-1] == "C":
            break

    print("Libros generados aleatoriamente:")
    print(f"[{', '.join(libros.items)}]")  

    lista_libros = sorted(libros.items)

    print("\nLibros ordenados de A a C:")
    print(f"[{', '.join(lista_libros)}]")  

if __name__ == "__main__":
    main()
