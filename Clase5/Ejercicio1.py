def definidor(numero):
    divisores = []
    for i in range(1, numero):
        if numero % i == 0:
            divisores.append(i)
    sumaDivisores = sum(divisores)
    return sumaDivisores == numero

numerosPerfectos = []

for i in range(1, 10000):
    if definidor(i):
        numerosPerfectos.append(i)

print("Los numeros perfectos ente 1 y 10000 son: ")
print(numerosPerfectos)