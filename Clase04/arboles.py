# comprension.py
import csv

# Ejercicio 4.16: Lista de altos de Jacarandá
def leer_arboles(nombre_archivo):
    arboleda = []
    with open(nombre_archivo, 'rt') as file:
        rows = csv.reader(file)
        headers = next(rows)
        types = [float, float, int, float, float, float, int, str, str, str, str, str, str, str, str, float, float]
        for row in rows:
            converted = [convert(value) for convert, value in zip(types, row)]
            arbol = dict(zip(headers, converted))
            arboleda.append(arbol)
    return arboleda

def dict_a_tuple(dict_data):
    return (dict_data['altura_tot'], dict_data['diametro'])

arboleda = leer_arboles('../Data/arbolado-en-espacios-verdes.csv')
H = [arbol['altura_tot'] for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']

# Ejercicio 4.17: Lista de altos y diámetros de Jacarandá
HyD = [dict_a_tuple(arbol) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']

# Ejercicio 4.18: Diccionario con medidas
def medidas_de_especies(especies, arboleda):
    return {especie: [dict_a_tuple(arbol) for arbol in arboleda if arbol['nombre_com'] == especie] for especie in especies}

def main():
    arboleda = leer_arboles('../Data/arbolado-en-espacios-verdes.csv')
    especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
    resultado = medidas_de_especies(especies, arboleda)
    for key, value in resultado.items():
        print(f'Hay {len(value)} arboles de tipo "{key}"')
