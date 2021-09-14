# costo_camion.py
# Ejercicio 2.2: Lectura de un archivo de datos

# costo = 0.0
# with open('../Data/camion.csv', 'rt') as file:
#     next(file)
#     for line in file:
#         product = line.split(',')
#         quantity = int(product[1])
#         price = float(product[2])
#         costo += quantity * price

# print(costo)

# Ejercicio 2.6: Transformar un script en una función
# def costo_camion(nombre_archivo):
#     '''
#     Recibe el nombre de un archivo con los datos de los productos en un camion
#     Y retorna el costo total de los mismos
    
#     Parameters
#     ----------
#     nombre_archivo : String
#         Devuelve el costo de la carga de un camion.

#     Returns
#     -------
#     Float
#     '''
#     costo = 0.0
#     with open(nombre_archivo, 'rt') as file:
#         next(file)
#         for line in file:
#             try:
#                 line = line[:-1]
#                 product = line.split(',')
#                 quantity = int(product[1])
#                 price = float(product[2])
#                 costo += quantity * price
#             except:
#                 print(f'WARNING: La linea "{line}" no es valida')
    
#     return costo

# costo = costo_camion('../Data/missing.csv')
# print('Costo total:', costo)

# Ejercicio 2.9: Funciones de la biblioteca
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
        for row in rows:
            try:
                product = row
                quantity = int(product[1])
                price = float(product[2])
                costo += quantity * price
            except:
                print(f'WARNING: La fila "{row}" no es valida')
    
    return costo

costo = costo_camion('../Data/camion.csv')
print('Costo total:', costo)

# Costo total: 47671.15
