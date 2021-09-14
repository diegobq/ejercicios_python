# envido.py
# Ejercicio 5.4: Envido
import random
from tqdm import tqdm


valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
palos = ['oro', 'copa', 'espada', 'basto']
mazo = [(valor, palo) for valor in valores for palo in palos]

def tirar_mano():
    mano = random.sample(mazo, k=3)
    return mano

def obtener_valor(valor):
    valor_envido = 0
    if valor < 10:
        valor_envido = valor
    return valor_envido

def calcular_puntos(carta1, carta2):
    puntos = 0
    palo1 = carta1[1]
    palo2 = carta2[1]
    puntos1 = obtener_valor(carta1[0])
    puntos2 = obtener_valor(carta2[0])
    if palo1 == palo2:
        puntos = puntos1 + puntos2 + 20
    else:
        puntos = max([puntos1, puntos2])
    
    return puntos
    

def puntos_envido():
    puntos = 0
    mano = tirar_mano()
    for i in range(3):
        carta1 = mano[i]
        for j in range(3):
            carta2 = mano[j]
            if i != j:
                total = calcular_puntos(carta1, carta2)
                if total > puntos:
                    puntos = total
    return puntos

def son_buenas(puntos):
    return 0 if puntos < 31 else 1

def prob_generala(N):
    G = sum([son_buenas(puntos_envido()) for i in tqdm(range(N))])
    prob = G/N
    return prob

print(prob_generala(10000))
