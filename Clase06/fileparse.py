# Ejercicio 6.9: Trabajando sin encabezados

import csv

def parse_csv(nombre_archivo, select = None, types = None, has_headers = True):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    '''
    with open(nombre_archivo) as f:
        filas = csv.reader(f)
        registros = []

        if has_headers:
            # Lee los encabezados del archivo
            encabezados = next(filas)
            types_func = types if types else [str] * len(encabezados)

            # Si se indicó un selector de columnas,
            #    buscar los índices de las columnas especificadas.
            # Y en ese caso achicar el conjunto de encabezados para diccionarios
    
            if select:
                indices = [encabezados.index(nombre_columna) for nombre_columna in select]
                encabezados = select
            else:
                indices = []
    
            for fila in filas:
                if not fila:    # Saltear filas vacías
                    continue
                # aplico los types
                fila = [func(value) for func, value in zip([func for func in types_func], fila)]

                # Filtrar la fila si se especificaron columnas
                if indices:
                    fila = [fila[index] for index in indices]
                

                # Armar el diccionario
                registro = dict(zip(encabezados, fila))
                registros.append(registro)
        else:
            registros = [fila for fila in filas if fila]
            if types:
                registros = [[func(value) for func, value in zip(types, fila)] for fila in registros]

    return registros
