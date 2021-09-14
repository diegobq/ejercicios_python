# arboles.py
import csv
import os
import matplotlib.pyplot as plt
import numpy as np

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

def medidas_de_especies(especies, arboleda):
    return {especie: [dict_a_tuple(arbol) for arbol in arboleda if arbol['nombre_com'] == especie] for especie in especies}

# Ejercicio 5.25: Histograma de altos de Jacarandás
def plot_H():
    nombre_archivo = os.path.join('..', 'Data', 'arbolado-en-espacios-verdes.csv')
    arboleda = leer_arboles(nombre_archivo)
    altos = [arbol['altura_tot'] for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']
    plt.hist(altos,bins=50)
    plt.show()
    
def show_scatter_hd(especie, hd_list):
    plt.xlim(0, 200)
    plt.ylim(0, 50)
    plt.xlabel("diametro (cm)")
    plt.ylabel("alto (m)")
    plt.title(f'Relación diámetro-alto para {especie}')
    pares = np.array(hd_list)
    h = pares[:, 0]
    d = pares[:, 1]
    plt.scatter(d,h, c = h)
    plt.show()
    
# Ejercicio 5.26: Scatterplot (diámetro vs alto) de Jacarandás
def scatter_hd():
    nombre_archivo = os.path.join('..', 'Data', 'arbolado-en-espacios-verdes.csv')
    arboleda = leer_arboles(nombre_archivo)
    especie = 'Jacarandá'
    hd_list = [dict_a_tuple(arbol) for arbol in arboleda if arbol['nombre_com'] == especie]
    show_scatter_hd(especie, hd_list)
    
# Ejercicio 5.27: Scatterplot para diferentes especies
def scatter_hd_especies():
    nombre_archivo = os.path.join('..', 'Data', 'arbolado-en-espacios-verdes.csv')
    arboleda = leer_arboles(nombre_archivo)
    especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
    medidas = medidas_de_especies(especies, arboleda)
    for (especie, valores) in medidas.items():
        show_scatter_hd(especie, valores)
