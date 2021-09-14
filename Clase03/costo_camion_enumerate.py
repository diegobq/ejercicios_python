# costo_camion.py
# Ejercicio 3.8: Un ejemplo práctico de enumerate()

import csv
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
        next(rows)
        for index, row in enumerate(rows):
            try:
                product = row
                quantity = int(product[1])
                price = float(product[2])
                costo += quantity * price
            except:
                print(f'WARNING: Fila {index + 1} "{row}" no es valida')
    
    return costo

costo = costo_camion('../Data/missing.csv')
print('Costo total:', costo)

# Costo total: 47671.15
