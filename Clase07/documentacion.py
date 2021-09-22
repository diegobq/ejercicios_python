# Ejercicio 7.10: Funciones y documentación

def valor_absoluto(n):
    '''
    Calcula el valor absoluto de n

    Parameters
    ----------
    n : TYPE int o float
        DESCRIPTION.
    
    Pre: n debe ser int o float

    Returns
    -------
    TYPE int o float
        DESCRIPTION: Retorna el valor absoluto de n.

    '''
    if n >= 0:
        return n
    else:
        return -n

def suma_pares(l):
    '''
    Calcula la suma de los elementos pares de una secuencia

    Parameters
    ----------
    l : TYPE
        DESCRIPTION.

    Pre: l debe ser una secuencia de int o float
    Pos: se devuelve la suma de todos los elementos pares de la secuencia
    Si la secuencia está vacía devuelve 0

    Returns
    -------
    res : TYPE
        DESCRIPTION.

    '''
    res = 0
    for e in l:
        if e % 2 ==0:
            res += e
        else:
            res += 0

    return res

def veces(a, b):
    '''
    Calcula el resultado de sumar a, b veces
    Pre: b tiene que ser entero mayor o igual a cero

    Parameters
    ----------
    a : TYPE int o float
        DESCRIPTION.
    b : TYPE int
        DESCRIPTION.

    Returns
    -------
    res : TYPE
        DESCRIPTION: la suma de a, b veces

    '''
    res = 0
    nb = b
    while nb != 0:
        #print(nb * a + res)
        res += a
        nb -= 1
    return res

def collatz(n):
    '''
    Itera hasta n sea igual a 1
    Durante la iteracion:
        Si n es par => n será n//2
        Si n es impar => n será 3 * n + 1

    Parameters
    ----------
    n : TYPE
        DESCRIPTION.

    Pre: n tiene que ser entero mayor que cero

    Returns
    -------
    res : TYPE
        DESCRIPTION.

    '''
    res = 1

    while n!=1:
        if n % 2 == 0:
            n = n//2
        else:
            n = 3 * n + 1
        res += 1

    return res
