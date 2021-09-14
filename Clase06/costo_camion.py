# costo_camion.py
# Ejercicio 6.12: Un poco más allá

import informe_funciones

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
    camion = informe_funciones.leer_camion(nombre_archivo)
    return sum([product['cajones'] * product['precio'] for product in camion])
