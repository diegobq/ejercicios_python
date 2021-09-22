# Ejercicio 7.8: Sumas

def sumar_enteros_ciclo(desde, hasta):
    entero_actual = desde
    resultado = 0
    while entero_actual <= hasta:
        resultado += entero_actual
        entero_actual += 1
    return resultado

def sumar_enteros_triangular(desde, hasta):
    resultado = 0
    if desde <= hasta:
        n = desde - 1
        m = hasta
        desde_triangular = n*(n+1)/2
        hasta_triangular = m*(m+1)/2
        resultado = int(hasta_triangular - desde_triangular)

    return resultado
