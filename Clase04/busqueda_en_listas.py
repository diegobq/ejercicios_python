# busqueda_en_listas.py

# Ejercicio 4.3: Búsquedas de un elemento
def buscar_u_elemento(lista, e):
    '''
        Devuelve la posicion de un elemento 'e' en una lista, 
        Devuelve 1 si el elemento no esta en la lista.-
    '''
    index = -1
    for i, elemento in enumerate(lista):
        if elemento == e:
            index = i

    return index

def buscar_n_elemento(lista, e):
    '''
        Devuelve la cantidad de ocurrencias de un elemento 'e' en una lista, 
    '''
    contador = 0
    for elemento in lista:
        if elemento == e:
            contador += 1
    
    return contador

def maximo(lista):
    '''Devuelve el maximo de una lista, 
    la lista debe ser no vacia.
    '''
    # m guarda el máximo de los elementos a medida que recorro la lista. 
    m = lista[0] # Lo inicializo con el primer elemento de la lista
    for e in lista: # Recorro la lista y voy guardando el mayor
        if e > m:
            m = e
    return m

def minimo(lista):
    '''Devuelve el minimo de una lista, 
    la lista debe ser no vacia.
    '''
    # m guarda el minimo de los elementos a medida que recorro la lista. 
    m = lista[0] # Lo inicializo con el primer elemento de la lista
    for e in lista: # Recorro la lista y voy guardando el menor
        if e < m:
            m = e
    return m

def main():
    buscar_u_elemento_test()
    buscar_n_elemento_test()
    maximo_test()
    minimo_test()

def buscar_u_elemento_test():
    print('TESTING: ', 'buscar_u_elemento_test', end=' => ')
    try:
        assert buscar_u_elemento([1,2,3,2,3,4],1) == 0, 'buscar_u_elemento_test'
        assert buscar_u_elemento([1,2,3,2,3,4],2) == 3, 'buscar_u_elemento_test'
        assert buscar_u_elemento([1,2,3,2,3,4],3) == 4, 'buscar_u_elemento_test'
        assert buscar_u_elemento([1,2,3,2,3,4],5) == -1, 'buscar_u_elemento_test'
        print('OK')
    except Exception:
        print('FAIL')
    
def buscar_n_elemento_test():
    print('TESTING: ', 'buscar_n_elemento_test', end=' => ')
    try:
        assert buscar_n_elemento([1,2,3,2,3,4],1) == 1, 'buscar_n_elemento_test'
        assert buscar_n_elemento([1,2,3,2,3,4],2) == 2, 'buscar_n_elemento_test'
        assert buscar_n_elemento([1,2,3,2,3,4],3) == 2, 'buscar_n_elemento_test'
        assert buscar_n_elemento([1,2,3,2,3,4],5) == 0, 'buscar_n_elemento_test'
        print('OK')
    except Exception:
        print('FAIL')

def maximo_test():
    print('TESTING: ', 'maximo', end=' => ')
    try:
        assert maximo([1,2,7,2,3,4]) == 7, 'maximo'
        assert maximo([1,2,3,4]) == 4, 'maximo'
        assert maximo([-5,4]) == 4, 'maximo'
        assert maximo([-5,-4]) == -4, 'maximo'
        print('OK')
    except Exception:
        print('FAIL')
    
def minimo_test():
    print('TESTING: ', 'minimo', end=' => ')
    try:
        assert minimo([1,2,7,2,3,4]) == 1, 'minimo'
        assert minimo([5,4,7,3,2,1]) == 1, 'minimo'
        assert minimo([-5,4]) == -5, 'minimo'
        assert minimo([-5,-4]) == -5, 'minimo'
        print('OK')
    except Exception:
        print('FAIL')
