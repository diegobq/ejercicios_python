# arboles.py
import csv
from collections import Counter

# Ejercicio 3.18: Lectura de los árboles de un parque
def leer_parque(nombre_archivo, parque):
    arboles = []
    
    with open(nombre_archivo, 'rt') as file:
        rows = csv.reader(file)
        encabezado = next(rows)
        for index, row in enumerate(rows):
            try:
                arbol = dict(zip(encabezado, row))
                if parque == None or arbol['espacio_ve'] == parque:
                    arbol['altura_tot'] = float(arbol['altura_tot'])
                    arboles.append(arbol)
            except:
                print(f'WARNING #{index}: "{row}" no es valida')
        
    return arboles

# Ejercicio 3.19: Determinar las especies en un parque
def especies(lista_arboles):
    especies = set()
    
    for arbol in lista_arboles:
        especies.add(arbol['nombre_com'])
    
    return especies

# Ejercicio 3.20: Contar ejemplares por especie
def contar_ejemplares(lista_arboles):
    ejemplares = Counter()
    for arbol in lista_arboles:
        nombre_ejemplar = arbol['nombre_com']
        ejemplares[nombre_ejemplar] += 1

    return ejemplares

# Ejercicio 3.21: Alturas de una especie en una lista
def obtener_alturas(lista_arboles, especie):
    alturas = []
    
    for arbol in lista_arboles:
        if arbol['nombre_com'] == especie:
            alturas.append(arbol['altura_tot'])
    
    return alturas

# Ejercicio 3.22: Inclinaciones por especie de una lista
def obtener_inclinaciones(lista_arboles, especie):
    inclinaciones = []

    for arbol in lista_arboles:
        if arbol['nombre_com'] == especie:
            inclinaciones.append(arbol['inclinacio'])

    return inclinaciones

# Ejercicio 3.23: Especie con el ejemplar más inclinado
def especimen_mas_inclinado(lista_arboles):
    inclinaciones_especie = {}
    especie_mas_inclinada = ('', 0)
    
    for arbol in lista_arboles:
        especie = arbol['nombre_com']
        if especie not in inclinaciones_especie.keys():
            inclinaciones_especie[especie] = []
        inclinaciones_especie[especie].append(int(arbol['inclinacio']))
    
    for especie in inclinaciones_especie.keys():
        inclinaciones = inclinaciones_especie[especie]
        max_inclinacion = max(inclinaciones)
        
        if max_inclinacion > especie_mas_inclinada[1]:
            especie_mas_inclinada = especie, max_inclinacion
    
    return especie_mas_inclinada

# Ejercicio 3.24: Especie más inclinada en promedio
def especie_promedio_mas_inclinada(lista_arboles):
    inclinaciones_especie = {}
    especie_mas_inclinada_promedio = ('', 0.0)
    
    for arbol in lista_arboles:
        especie = arbol['nombre_com']
        if especie not in inclinaciones_especie.keys():
            inclinaciones_especie[especie] = []
        inclinaciones_especie[especie].append(int(arbol['inclinacio']))
    
    for especie in inclinaciones_especie.keys():
        inclinaciones = inclinaciones_especie[especie]
        promedio = sum(inclinaciones) / len(inclinaciones)
        
        if promedio > especie_mas_inclinada_promedio[1]:
            especie_mas_inclinada_promedio = especie, promedio
    
    return especie_mas_inclinada_promedio

def main():
    nombre_archivo = '../Data/arbolado-en-espacios-verdes.csv'
    parque = "GENERAL PAZ"
    arboles = leer_parque(nombre_archivo, parque)
    print(f'Ej 3.18: Hay "{len(arboles)}" arboles en el parque "{parque}"')
    
    arboles = leer_parque(nombre_archivo, None)
    tipos_especie = especies(arboles)
    print(f'\nEj 3.19: Hay "{len(tipos_especie)}" especies en todos los parques')
    
    parques = [
        {'nombre': 'General Paz', 'espacio_ve': 'GENERAL PAZ'},
        {'nombre': 'Los Andes', 'espacio_ve': 'ANDES, LOS'},
        {'nombre': 'Centenario', 'espacio_ve': 'CENTENARIO'}
    ]
    mas_comunes_parque = {}
    encabezado = ''
    separador = '-'
    formato = '30s'
    numero_mas_comunes = 5
    for parque in parques:
        nombre_parque = parque['nombre']
        espacio_verde = parque['espacio_ve']
        arboles = leer_parque(nombre_archivo, espacio_verde)
        mas_comunes = contar_ejemplares(arboles).most_common(numero_mas_comunes)
        mas_comunes_parque[nombre_parque] = mas_comunes
        encabezado += f'{nombre_parque:{formato}}'  
    
    print('\nEj 3.20: Cantidad de especies mas comunes por parque')
    print(encabezado)
    print(separador * len(encabezado))
    for index in range(numero_mas_comunes):
        fila = ''
        for parque in parques:
            nombre_parque = parque['nombre']
            especie, cantidad = mas_comunes_parque[nombre_parque][index]
            mas_comun_str = f'{especie}: {cantidad}'
            fila += f'{mas_comun_str:{formato}}'
        print(fila)
        
    parques = [
        {'nombre': 'General Paz', 'espacio_ve': 'GENERAL PAZ'},
        {'nombre': 'Los Andes', 'espacio_ve': 'ANDES, LOS'},
        {'nombre': 'Centenario', 'espacio_ve': 'CENTENARIO'}
    ]
    formato = '15s'
    encabezado = f'{"Medida":{formato}}' 
    mas_altos = f'{"max":{formato}}' 
    promedio_alturas = f'{"prom":{formato}}' 
    separador = '-'
    formatoFloat = '<15.2f'
    especie = 'Jacarandá'
    for parque in parques:
        nombre_parque = parque['nombre']
        espacio_verde = parque['espacio_ve']
        arboles = leer_parque(nombre_archivo, espacio_verde)
        alturas = obtener_alturas(arboles, especie)
        maxima_altura = max(alturas)
        promedio_altura = sum(alturas) / len(alturas)
        encabezado += f'{nombre_parque:{formato}}' 
        mas_altos += f'{maxima_altura:{formatoFloat}}'
        promedio_alturas += f'{promedio_altura:{formatoFloat}}'
    
    print('\nEj 3.21: Alturas de una especie por parque')
    print(encabezado)
    print(separador * len(encabezado))
    print(mas_altos)
    print(promedio_alturas)
    
    print('\nEj 3.22: Inclinaciones por especie de una lista')
    especie = 'Jacarandá'
    inclinaciones = obtener_inclinaciones(arboles, especie)
    print(inclinaciones)
    
    print('\nEj 3.23: Especie con el ejemplar más inclinado')
    parque = 'GENERAL PAZ'
    arboles = leer_parque(nombre_archivo, parque)
    max_inclinacion_especie = especimen_mas_inclinado(arboles)
    print(max_inclinacion_especie)
    
    print('\nEj 3.24: Especie más inclinada en promedio')
    parque = 'ANDES, LOS'
    arboles = leer_parque(nombre_archivo, parque)
    max_inclinacion_promedio_especie = especie_promedio_mas_inclinada(arboles)
    print(max_inclinacion_promedio_especie)
    
    return None
