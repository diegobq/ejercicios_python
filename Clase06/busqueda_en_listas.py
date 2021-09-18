# busqueda_en_listas.py

# Ejercicio 6.13: Búsqueda lineal sobre listas ordenadas
def busqueda_binaria(lista, e, verbose = False):
    '''
        Devuelve la posicion de un elemento 'e' en una lista ordenada, 
        Devuelve -1 si el elemento no esta en la lista.-
    '''
    index = -1
    list_size = len(lista)
    izq = 0
    der = len(lista) - 1
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
            if verbose:
                print(f'Izquierda: ({izq}, {der})')
        elif e > middle_value:
            izq = middle_index + 1
            if verbose:
                print(f'Derecha: ({izq}, {der})')

    return index

def main():
    busqueda_binaria_test()

def busqueda_binaria_test():
    print('TESTING: ', 'busqueda_binaria', end=' => ')
    try:
        assert busqueda_binaria([],2) == -1, 'busqueda_binaria'
        
        assert busqueda_binaria([1],2) == -1, 'busqueda_binaria'
        assert busqueda_binaria([1,3],2) == -1, 'busqueda_binaria'
        assert busqueda_binaria([1,3,4],2) == -1, 'busqueda_binaria'
        
        assert busqueda_binaria([2],2) == 0, 'busqueda_binaria'
        assert busqueda_binaria([2,3],2) == 0, 'busqueda_binaria'
        assert busqueda_binaria([1,2,3],2) == 1, 'busqueda_binaria'
        assert busqueda_binaria([1,2,3,4],2) == 1, 'busqueda_binaria'
        assert busqueda_binaria([1,2,3,4],3) == 2, 'busqueda_binaria'

        assert busqueda_binaria([2,3,4],2) == 0, 'busqueda_binaria'
        assert busqueda_binaria([2,3,4,5],2) == 0, 'busqueda_binaria'
        
        assert busqueda_binaria([2,3,4],4) == 2, 'busqueda_binaria'
        assert busqueda_binaria([2,3,4,5],4) == 2, 'busqueda_binaria'
        print('OK')
    except Exception:
        print('FAIL')

main()
