import random ##Se importa el módulo random
import time 

def calcular_porcentaje_pares(n): ##Se define una funcipon que tome parametros n
    numeros = [random.randint(1, 1000) for _ in range(n)] ##Se generan n numeros aleatorios y se guardan en un vector
    numeros_pares = [num for num in numeros if num % 2 == 0] ##Se crea otro vector y en este solo se guardan los numeros pares
    porcentajes_pares = (len(numeros_pares) / n) * 100 ##Se calcula el porcentaje de números pares
    return porcentajes_pares ##Regresa el porcentaje de pares generados

cantidad_numeros = int(input("Ingrese la cantidad de números a generar: ")) ##Se pide el número n de numeros a generar

while cantidad_numeros<=0:
    print("Tamaño incorrecto del vector")
    cantidad_numeros = int(input("Ingrese la cantidad de números a generar: "))

inicio_tiempo = time.time()
porcentaje_pares= calcular_porcentaje_pares(cantidad_numeros)
fin_tiempo = time.time()

tiempo_ejecucion = fin_tiempo - inicio_tiempo

print(f"El porcentaje de números pares generados es: {porcentaje_pares:.2f}%")
print(f"El tiempo de ejecución es de: {tiempo_ejecucion:.4f} segundos")

