# Ejercicio 7.7: Arreglemos las funciones existentes

import csv
from fileparse import parse_csv
import sys
import lote
import formato_tabla

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
    lotes = []
    with open(nombre_archivo) as f:
        filas = csv.reader(f)
        camion = parse_csv(filas, types=[str, int, float])
        for producto in camion:
            nombre = producto['nombre']
            cajones = producto['cajones']
            precio = producto['precio']
            miLote = lote.Lote(nombre, cajones, precio)
            lotes.append(miLote)
    
    return lotes

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
    with open(nombre_archivo) as f:
        filas = csv.reader(f)
        rows = parse_csv(filas, types=[str, float], has_headers=False)
        precios = {name: price for name, price in rows}

    return precios

def hacer_informe(camion, precios):
    resultado = []
    for producto in camion:
        nombre = producto.nombre
        cajones = producto.cajones
        precio = producto.precio
        precio_str = producto.precio_str()
        precio_venta = precios[nombre]
        diferencia = precio_venta - precio

        resultado.append({'nombre': nombre, 'cajones': cajones, 'precio': precio_str, 'diferencia': diferencia})
        
    return resultado

def imprimir_informe(informe, formateador):
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    formateador.encabezado(headers)
    for item in informe:
        formateador.fila(item.values())

def informe_camion(nombre_archivo_camion, nombre_archivo_precios, fmt = 'txt'):
    camion = leer_camion(nombre_archivo_camion)
    precios = leer_precios(nombre_archivo_precios)
    informe = hacer_informe(camion, precios)
    formateador = formato_tabla.crear_formateador(fmt)
    imprimir_informe(informe, formateador)
    
def f_principal(argv):
    if len(argv) < 3:
        nombre_archivo =argv[0]
        parametros = 'archivo_camion archivo_precios'
        raise SystemExit(f'Uso adecuado: {nombre_archivo} {parametros}')
    
    nombre_archivo_camion = argv[1]
    nombre_archivo_precios = argv[2]
    fmt = 'txt'
    if (len(argv) == 4):
        fmt = argv[3]
    informe_camion(nombre_archivo_camion, nombre_archivo_precios, fmt)

if __name__ == '__main__':
    f_principal(sys.argv)
