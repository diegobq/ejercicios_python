# propaga.py

# Ejercicio 4.6: Propagación
def propagar(lista):
    NUEVO = 0
    ENCENDIDO = 1
    CARBONIZADO = -1
    propagada = []
    fosforos_previos = []
    necesita_propagar = False

    for i, fosforo in enumerate(lista):
        fosforo_propagado = fosforo
        if fosforo == NUEVO:
            if necesita_propagar:
                # encendemos el fosforo nuevo
                fosforo_propagado = ENCENDIDO
            else:
                # guardamos la posicion en fosforos_previos
                fosforos_previos.append(i)
        elif fosforo == CARBONIZADO:
            # no hay propagacion hacia adelante
            necesita_propagar = False
            # no hay propagacion hacia atras
            fosforos_previos = []
        elif fosforo == ENCENDIDO:
            # hay propagacion hacia adelante
            necesita_propagar = True
            # propagamos hacia atras
            for index_fosforo_previo in fosforos_previos:
                propagada[index_fosforo_previo] = ENCENDIDO
        
        propagada.append(fosforo_propagado)
    
    return propagada

def main():
    propagar_test()

def propagar_test():
    test1 = [ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0]
    test1_propagado = [ 0, 0, 0,-1, 1, 1, 1, 1,-1, 1, 1, 1, 1]
    test2 = [ 0, 0, 0, 1, 0, 0]
    test2_propagado = [ 1, 1, 1, 1, 1, 1]
    print('TESTING: ', 'propagar', end=' => ')
    try:
        assert propagar(test1).__eq__(test1_propagado), 'propagar'
        assert propagar(test2).__eq__(test2_propagado), 'propagar'
        print('OK')
    except Exception:
        print('FAIL')
