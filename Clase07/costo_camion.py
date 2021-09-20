# costo_camion.py
# Ejercicio 7.7: Arreglemos las funciones existentes

import sys
import informe_final

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
    camion = informe_final.leer_camion(nombre_archivo)
    return sum([product['cajones'] * product['precio'] for product in camion])

def f_principal(argv):
    nombre_archivo = argv[0]
    if not len(argv) == 2:
        parametros = 'nombre_archivo'
        raise SystemExit(f'Uso adecuado: {nombre_archivo} {parametros}')

    parametros = argv[1]
    costo = costo_camion(parametros)
    print(f'Costo total: {costo}')
    return

if __name__ == '__main__':
    f_principal(sys.argv)
