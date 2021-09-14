# figuritas.py
# Ejercicio 5.15
import random
import numpy as np

def crear_album(figus_total):
    return np.zeros(figus_total)

def album_incompleto(A):
    return len(A[A == 0]) != 0

def comprar_figu(figus_total):
    return random.randint(1, figus_total)

def cuantas_figus(figus_total):
    album = crear_album(figus_total)
    figus_compradas = 0
    while album_incompleto(album):
        nueva_figu = comprar_figu(figus_total)
        album[nueva_figu - 1] += 1
        figus_compradas += 1
    
    return figus_compradas

def experimento_figus(n_repeticiones, figus_total):
    l = [cuantas_figus(figus_total) for i in range(n_repeticiones)]
    
    return np.mean(l)
