"""password = input("Ingrese contraseña debe tener 3 dígitos: ")

def tresDigitos(numero):
    numero_como_cadena = str(numero)
    return len(numero_como_cadena) == 3

tresDigitos = False 

for i in range(0, 1000):
    if tresDigitos(i):
        print(i)
        if password == str(i).zfill(3):
            print("Se encontró la contraseña: " + password)
            tiene_tres_digitos_valido = True
            break

if not tresDigitos:
    print("La contraseña no tiene 3 dígitos")"""

clave = input("Digite clave: ")
c = 0
for i in range(0,10):
    for j in range(0,10):
        for k in range (0,10):
            c+=1
            if clave == str(i) + str(j) + str(k):
                print("La clave es: ", str(i) + str(j) + str(k) + " obtenida en ", c, " intentos.")
                break