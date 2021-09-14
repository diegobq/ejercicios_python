# costo_camion_zip.py
# Ejercicio 3.9: La función zip

import csv
from pprint import pprint

def costo_camion(nombre_archivo):
    '''
    Recibe el nombre de un archivo con los datos de los productos en un camion
    Y retorna el costo total de los mismos
    
    Parameters
    ----------
    nombre_archivo : String
        Devuelve el costo de la carga de un camion.

    Returns
    -------
    Float
    '''
    costo = 0.0
    with open(nombre_archivo, 'rt') as file:
        rows = csv.reader(file)
        encabezado = next(rows)
        for index, row in enumerate(rows, start=1):
            product = dict(zip(encabezado, row))
            try:
                quantity = int(product['cajones'])
                price = float(product['precio'])
                costo += quantity * price
            except:
                print(f'WARNING: Fila {index} "{product}" no es valida')
    
    return costo

costo = costo_camion('../Data/fecha_camion.csv')
print('Costo total:', costo)

# Costo total: 47671.15
