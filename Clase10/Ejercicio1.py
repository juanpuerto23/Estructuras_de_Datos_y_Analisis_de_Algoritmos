frase = input("Digite la frase: ")
lista = []
lista = frase.split(" ")
if len(lista) > 9:
    c = 0
    for x in lista:
        if c % 2 == 0:
            lista[c] = "X"
        c += 1
print("Frase convertida: ", lista)

## Unir la frase en la lista sin metodos
acu = ""
for x in lista:
    acu += str(x) + " "
print("Frase resultante: ",acu)