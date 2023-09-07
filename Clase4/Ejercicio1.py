import random 
import time

def ordenar_rapido(arr):
    if len(arr) <= 1:
        return arr
    pivote = arr[len(arr) // 2]
    izquierda = [x for x in arr if x < pivote]
    medio = [x for x in arr if x == pivote]
    derecha = [x for x in arr if x > pivote]
    return ordenar_rapido(izquierda) + medio + ordenar_rapido(derecha)

def main():
    n = int(input("Ingrese la cantidad de números pares a generar: "))
    numeros_pares_aleatorios = [random.randint(2, 100) * 2 for _ in range(n)]
    promedio = sum(numeros_pares_aleatorios) / n
    menores_al_promedio = [num for num in numeros_pares_aleatorios if num < promedio]
    
    print("Números generados:", numeros_pares_aleatorios)
    print("Promedio:", promedio)
    print("Números menores al promedio:", menores_al_promedio)
    
    if len(menores_al_promedio) < n / 2:
        print("Aplicando Ordenamiento Rápido a los números menores al promedio...")
        menores_ordenados = ordenar_rapido(menores_al_promedio)
        print("Números menores al promedio ordenados:", menores_ordenados)

if __name__ == "__main__":
    main()