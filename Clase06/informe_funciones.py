# Ejercicio 6.11: Usemos tu modulo

from fileparse import parse_csv

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
    camion = parse_csv(nombre_archivo, types=[str, int, float])
    
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
    rows = parse_csv(nombre_archivo, types=[str, float], has_headers=False)
    precios = {name: price for name, price in rows}
    
    return precios

def hacer_informe(camion, precios):
    resultado = []
    for lote in camion:
        nombre = lote['nombre']
        cajones = lote['cajones']
        precio = lote['precio']
        precio_str = '$' + str(precio)
        precio_venta = precios[nombre]
        diferencia = precio_venta - precio

        resultado.append({'nombre': nombre, 'cajones': cajones, 'precio': precio_str, 'diferencia': diferencia})
        
    return resultado

def imprimir_header():
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    separaciones = tuple(['-' * 10] * 4)
    formats = '%10s ' * 4 
    
    print(formats % headers)
    print(formats % separaciones)

def imprimir_body(informe):
    for item in informe:
        nombre = item['nombre']
        cajones = item['cajones']
        precio = item['precio']
        diferencia = item['diferencia']
        print(f'{nombre:>10s} {cajones:10d} {precio:>10s} {diferencia:10.2f}')

def imprimir_informe(informe):
    imprimir_header()
    imprimir_body(informe)

def informe_camion(nombre_archivo_camion, nombre_archivo_precios):
    camion = leer_camion(nombre_archivo_camion)
    precios = leer_precios(nombre_archivo_precios)
    informe = hacer_informe(camion, precios)
    imprimir_informe(informe)

# informe_camion('../Data/camion.csv', '../Data/precios.csv')