# inclusive.py
# Ejercicio 1.29: Traductor (rústico) al lenguaje inclusivo¶

frase = 'Todos, tu también'
palabras = frase.split(' ')
palabras_traducidas = []
vocales_no_inclusivas = ['o', 'a']

for palabra in palabras:
    if (palabra[-1] in vocales_no_inclusivas):
    	palabra_inclusiva = palabra[:-1] + 'e'
    elif (palabra[-2] in vocales_no_inclusivas):
        palabra_inclusiva = palabra[:-2] + 'e' + palabra[-1]
    else:
    	palabra_inclusiva = palabra
    palabras_traducidas.append(palabra_inclusiva)
    
print(' '.join(palabras_traducidas))


# todes somes programadores
