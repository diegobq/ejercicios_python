# tabla_informe.py
# Ejercicio 3.16: Un desafío de formato

import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    '''
    Recibe el nombre de un archivo con los datos de los productos en un camion
    Y retorna una lista de los lotes
    
    Parameters
    ----------
    nombre_archivo : String
        Nombre del archivo del que se obtendran los datos.

    Returns
    -------
    List
    '''
    camion = []
    with open(nombre_archivo, 'rt') as file:
        rows = csv.reader(file)
        encabezado = next(rows)
        for index, row in enumerate(rows, start=1):
            try:
                product = dict(zip(encabezado, row))
                product['cajones'] = int(product['cajones'])
                product['precio'] = float(product['precio'])
                camion.append(product)
            except:
                print(f'WARNING #{index}: La linea "{product}" no es valida')
    
    return camion

def leer_precios(nombre_archivo):
    '''
    Recibe el nombre de un archivo con los precios de venta de los productos
    Y generar un diccionario con el precio de cada producto

    Parameters
    ----------
    nombre_archivo : String
        Nombre del archivo del que se obtendran los datos.

    Returns
    -------
    Dictionary.

    '''
    precios = {}
    with open(nombre_archivo, 'rt') as file:
        rows = csv.reader(file)
        for row in rows:
            try:
                if len(row) == 2:
                    name = row[0]
                    price = float(row[1])
                    precios[name] = price
            except:
                print(f'WARNING: La linea "{row}" no es valida')
    
    return precios

def imprimir_header():
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    separaciones = tuple(['-' * 10] * 4)
    formats = '%10s ' * 4 
    
    print(formats % headers)
    print(formats % separaciones)
    return

def informe():
    camion = leer_camion('../Data/fecha_camion.csv')
    precios = leer_precios('../Data/precios.csv')
    imprimir_header()
    for lote in camion:
        nombre = lote['nombre']
        cajones = lote['cajones']
        precio = lote['precio']
        precio_str = '$' + str(precio)
        precio_venta = precios[nombre]
        diferencia = precio_venta - precio
        print(f'{nombre:>10s} {cajones:10d} {precio_str:>10s} {diferencia:10.2f}')

informe()