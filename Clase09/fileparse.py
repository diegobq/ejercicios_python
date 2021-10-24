# Ejercicio 7.6: De archivos a "objetos cual archivos"

def parse_csv(filas, select = None, types = None, has_headers = True, silence_errors = False):
    '''
    Parsea una lista de registros.
    select: Se puede seleccionar sólo un subconjunto de las columnas. Debe ser una lista de nombres de las columnas a considerar.
    types: castea los valores a un tipo de dato. Debe ser una lista de funciones
    has_headers: true si la primera linea son nombres de headers
    '''
    if not has_headers and select:
        raise RuntimeError('Para seleccionar, necesito encabezados.')

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

        for i, fila in enumerate(filas, 1):
            if not fila:    # Saltear filas vacías
                continue
            try:
                # aplico los types
                fila = [func(value) for func, value in zip([func for func in types_func], fila)]
            except ValueError as e:
                if not silence_errors:
                    print(f'Fila {i}: No pude convertir {fila}')
                    print(f'Fila {i}: Motivo: {e}')
                continue

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



