# bbin.py

# Ejercicio 6.13: Búsqueda lineal sobre listas ordenadas
def donde_insertar(lista, e, verbose = False):
    '''
        Devuelve la posicion de un elemento 'e' en una lista ordenada, 
        Devuelve -1 si el elemento no esta en la lista.-
    '''
    index = -1
    list_size = len(lista)
    izq = 0
    der = len(lista) - 1
    middle_index = 0
    a_der = 0
    while izq <= der and index == -1:
        middle_index = (izq + der) // 2
        middle_value = lista[middle_index]
        if verbose:
            print(f'***Size: {list_size}***')
            print(f'Middle: {middle_value}')
        if middle_value == e:
            index = middle_index
        elif e < middle_value:
            der = middle_index - 1
            a_der = 0
            if verbose:
                print(f'Izquierda: ({izq}, {der})')
        elif e > middle_value:
            izq = middle_index + 1
            a_der = 1
            if verbose:
                print(f'Derecha: ({izq}, {der})')
    if index == -1:
        index = middle_index + a_der

    return index

def insertar(lista, e, verbose = False):
    index = donde_insertar(lista, e, verbose)
    if index >= len(lista):
        lista.append(e)
    elif not lista[index] == e:
        lista.insert(index, e)
        
    return index
    