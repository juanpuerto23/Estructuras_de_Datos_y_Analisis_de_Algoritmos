import random
categoria_libro = ['A', 'B', 'C']
m = int(input("Libros a generar: "))
while True:
    libros = random.choices(categoria_libro, k = m)
    if libros[0] == 'A' and libros[-1] == 'C':
        print(libros)
        break