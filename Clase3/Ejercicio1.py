import random
import time

tiempoInicio = time.time()

def ordenarRapido(arr):
    if len(arr) <= 1:
        return arr
    pivote = arr[len(arr) // 2]
    izquierda = [x for x in arr if x < pivote]
    medio = [x for x in arr if x == pivote]
    derecha = [x for x in arr if x > pivote]
    return ordenarRapido(izquierda) + medio + ordenarRapido(derecha)

def arregloAleatorio(n):
    return [random.randint(1, 200) for _ in range(n)]

numElementos = int(input("Ingresa el número del vector: "))

arreglo = arregloAleatorio(numElementos)
print("Vector original:", arreglo)


arregloOrdenado = ordenarRapido(arreglo)


print("Vector ordenado:", arregloOrdenado)
tiempoFin = time.time()
print(f"Tiempo de ejecución: {tiempoFin - tiempoInicio:.4f} segundos")