# cocumple.py
# Ejercicio 5.3: Cocumpleaños
import random
from collections import Counter

def hay_repetidos(cantidad_personas):
    cumples = Counter()
    repetido = 0
    i = 0
    while i < cantidad_personas and repetido == 0:
        dia = random.randint(1, 365)
        cumples[dia] += 1
        if cumples[dia] > 1:
            repetido = 1
        i += 1

    return repetido

def prob_cocumple(N):
    G = sum([hay_repetidos(30) for i in range(N)])
    prob = G/N
    return prob
        
print(prob_cocumple(1000))
