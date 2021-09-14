# camion_commandline.py
# Ejercicio 2.10: Ejecución desde la línea de comandos con parámetros
import csv
import sys

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
        for row in rows:
            try:
                product = row
                quantity = int(product[1])
                price = float(product[2])
                costo += quantity * price
            except:
                print(f'WARNING: La fila "{row}" no es valida')
    
    return costo

if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = '../Data/camion.csv'

costo = costo_camion(nombre_archivo)
print('Costo total:', costo)

# Costo total: 47671.15
