def busqueda_lineal(lista, e):
    index = -1
    for i, elemento in enumerate(lista):
        if e == elemento:
            index = i
            break
    return index

lista = [1,2,3,4,5,6]
index = busqueda_lineal(lista, 4)
print(f'Index: {index}')
