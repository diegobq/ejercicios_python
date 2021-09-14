# informe.py
# Ejercicio 2.18: Balances
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
        next(file)
        rows = csv.reader(file)
        for row in rows:
            try:
                name = row[0]
                quantity = int(row[1])
                price = float(row[2])
                lote = {}
                lote['nombre'] = name
                lote['cajones'] = quantity
                lote['precio'] = price
                camion.append(lote)
            except:
                print(f'WARNING: La linea "{row}" no es valida')
    
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

def informe():
    camion = leer_camion('../Data/camion.csv')
    precios = leer_precios('../Data/precios.csv')
    costo_total = 0
    precio_total = 0
    diferencia_total = 0
    print(f'{"Producto":10s} {"Costo":>10s} {"Precio":>10s} {"Diferencia":>11s} |')
    print('=============================================|')
    for lote in camion:
        producto = lote['nombre']
        costo = lote['precio']
        precio = precios[producto]
        diferencia = precio - costo
        costo_total += costo
        precio_total += precio
        diferencia_total += diferencia
        print(f'{producto:10s} {costo:10.2f} {precio:10.2f} {diferencia:11.2f} |')
    print('=============================================|')
    print(f'{"Total":10s} {costo_total:10.2f} {precio_total:10.2f} {diferencia_total:11.2f} |\n')
    
    print(f'Costo camion: {round(costo_total, 2)}')
    print(f'Recaudacion de Venta: {round(precio_total, 2)}')
    print(f'Diferencia: {diferencia_total}')
    print('Ganancia' if diferencia_total > 0  else 'Pérdida')

informe()