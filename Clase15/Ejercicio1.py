def corrector_ortografico(frase, sugerencias):
    palabras = frase.split()
    for i, palabra in enumerate(palabras):
        if palabra in sugerencias:
            print(f'La palabra "{palabra}" puede tener errores. Deseas corregirla? (Si/No)')
            respuesta = input().lower()
            if respuesta == 'Si':
                print(f'Posibles correciones para "{palabra}":')
                for j, correcion in enumerate(sugerencias[palabra]):
                    print(f'{j+1}. {correcion}')
                opcion = int(input(f'Elige una opcion (1-{len(sugerencias[palabra])}):'))
                palabras[i] = sugerencias[palabra][opcion-1]
    nueva_frase = ' '.join(palabras)
    return nueva_frase

diccionario = { 
    'hola' : ['bola', 'sola', 'cola'],
    'mundo': ['hundo', 'pundo', 'lundo']
    }

frase_usuario = input("Introduce una frase")
nueva_frase = corrector_ortografico(frase_usuario, diccionario)
print(f'La nueva frase es "{nueva_frase}"')