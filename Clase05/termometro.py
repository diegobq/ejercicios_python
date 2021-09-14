# termometro.py
# Ejercicio 5.8: Guardar temperaturas
import math
import random
import numpy as np

def medir_temp(n):
    mediciones = np.empty(n)
    temperatura = 37.5
    sigma = 0.2
    for i in range(n):
        medicion = random.normalvariate(temperatura,sigma)
        mediciones[i] = medicion
    
    np.save('../Data/temperaturas.npy', mediciones)
    return mediciones

def obtener_mediana(mediciones):
    size = len(mediciones)
    mitad = math.ceil(size / 2) - 1
    mediana = mediciones[mitad]
    if size % 2 == 0:
        proxima = mediciones[mitad + 1]
        mediana = (mediana + proxima) / 2
    
    return mediana

def resumen_temp(n):
    mediciones = medir_temp(n)
    mediciones.sort()
    medicion_minima = mediciones[0]
    medicion_maxima = mediciones[-1]
    medicion_promedio = sum(mediciones) / n
    medicion_mediana = obtener_mediana(mediciones)
    return (medicion_maxima, medicion_minima, medicion_promedio, medicion_mediana)
