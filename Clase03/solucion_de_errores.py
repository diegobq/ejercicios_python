# solucion_de_errores.py


#%%
# Ejercicio 3.1: Semántica
# Comentario: El error era que el return False corta el ciclo.
#   Lo corregí:
#       + cortando sólo la ejecución cuando es True
#       + y retornando False si no contiene a
#       + no distingue mayúsculas de minúsculas
#    A continuación va el código corregido
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        i += 1
    
    return False

tiene_a('UNSAM 2020')
tiene_a('abracadabra')
tiene_a('La novela 1984 de George Orwell')

#%%
# Ejercicio 3.2: Sintaxis
# Comentario: El error era que tenía errores e sintaxis
#   Lo corregí:
#       + agregando ":" en las estructuras que lo requieren
#       + returnando False. Antes decía Falso
#    A continuación va el código corregido
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        i += 1
    return False

tiene_a('UNSAM 2020')
tiene_a('La novela 1984 de George Orwell')

#%%
# Ejercicio 3.3: Tipos
# Comentario: El error era que no valida que la expresion sea un string
#   Lo corregí:
#       + convirtiendo el input de la funcion en un string
#    A continuación va el código corregido
def tiene_uno(expresion):
    expresion_str = str(expresion)
    n = len(expresion_str)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion_str[i] == '1':
            tiene = True
        i += 1
    return tiene

#%%
# Ejercicio 3.4: Alcances
# Comentario: El error era que la función no retornaba nada entonces c = None
#   Lo corregí:
#       + retornando el valor de la entre a y b
#    A continuación va el código corregido
tiene_uno('UNSAM 2020')
tiene_uno('La novela 1984 de George Orwell')
tiene_uno(1984)

def suma(a,b):
    return a + b

a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")

#%%
# Ejercicio 3.5: Pisando memoria
# Comentario: El error era que la variable registro que se agrega al camión es la misma en cada iteración
#   Lo corregí:
#       + creando una nueva variable registro en cada iteración
#    A continuación va el código corregido
import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro={}
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion

camion = leer_camion('../Data/camion.csv')
pprint(camion)


