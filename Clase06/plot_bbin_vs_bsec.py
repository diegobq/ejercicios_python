import random
import matplotlib.pyplot as plt
import numpy as np

def generar_lista(n, m):
    l = random.sample(range(m), k = n)
    l.sort()
    return l

def generar_elemento(m):
    return random.randint(0, m-1)

def busqueda_secuencial_(lista, x):
    '''Si x está en la lista devuelve el índice de su primera aparición, 
    de lo contrario devuelve -1. Además devuelve la cantidad de comparaciones
    que hace la función.
    '''
    comps = 0 # inicializo en cero la cantidad de comparaciones
    pos = -1
    for i,z in enumerate(lista):
        comps += 1 # sumo la comparación que estoy por hacer
        if z == x:
            pos = i
            break
    return pos, comps

def busqueda_binaria(lista, e):
    '''
        Devuelve la posicion de un elemento 'e' en una lista ordenada, 
        Devuelve -1 si el elemento no esta en la lista.-
    '''
    comps = 0 # inicializo en cero la cantidad de comparaciones
    index = -1
    izq = 0
    der = len(lista) - 1
    while izq <= der and index == -1:
        middle_index = (izq + der) // 2
        middle_value = lista[middle_index]

        if middle_value == e:
            index = middle_index
        elif e < middle_value:
            der = middle_index - 1
            comps += 1
        elif e > middle_value:
            izq = middle_index + 1
            comps += 1

    return (index, comps)

def experimento_secuencial_promedio(lista, m, k):
    comps_tot = 0
    for i in range(k):
        x = generar_elemento(m)
        comps_tot += busqueda_secuencial_(lista,x)[1]

    comps_prom = comps_tot / k
    return comps_prom

def experimento_binario_promedio(lista, m, k):
    comps_tot = 0
    for i in range(k):
        x = generar_elemento(m)
        comps_tot += busqueda_binaria(lista,x)[1]

    comps_prom = comps_tot / k
    return comps_prom

def graficar_bbin_vs_bseq(m, k):
    largos = np.arange(256) + 1 # estos son los largos de listas que voy a usar
    # lista de largo i, para i entre 1 y 256
    comps_secuencial_promedio = np.zeros(256) # aca guardo el promedio de comparacion secuencial
    comps_binaria_promedio = np.zeros(256) # aca guardo el promedio de comparacion binaria
    
    for i, n in enumerate(largos):
        lista = generar_lista(n, m) # genero lista de largo n
        comps_secuencial_promedio[i] = experimento_secuencial_promedio(lista, m, k)
        comps_binaria_promedio[i] = experimento_binario_promedio(lista, m, k)
    
    # ahora grafico largos de listas contra operaciones promedio de búsqueda.
    plt.plot(largos,comps_secuencial_promedio,label = 'Búsqueda Secuencial')
    plt.plot(largos,comps_binaria_promedio,label = 'Busqueda Binaria')
    plt.xlabel("Largo de la lista")
    plt.ylabel("Cantidad de comparaciones")
    plt.title("Complejidad de Búsqueda secuencial vs Binaria")
    plt.ylim(1, 30)
    plt.legend()
    plt.show()
