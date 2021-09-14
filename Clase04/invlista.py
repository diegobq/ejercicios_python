# invlista.py

# Ejercicio 4.5: Invertir una lista
def invertir_lista(lista):
    invertida = []
    for e in lista: # Recorro la lista
        # agrego el elemento e al principio de la lista invertida
        invertida.insert(0, e)
    return invertida

def main():
    invertir_lista_test()

def invertir_lista_test():
    ciudades = ['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel']
    sedaduic = ['San Miguel', 'San Fernando', 'Santiago', 'Rosario', 'Bogotá']
    print('TESTING: ', 'invertir_lista', end=' => ')
    try:
        assert invertir_lista([1, 2, 3, 4, 5]).__eq__([5,4,3,2,1]), 'invertir_lista'
        assert invertir_lista(ciudades).__eq__(sedaduic), 'invertir_lista'
        print('OK')
    except Exception:
        print('FAIL')
