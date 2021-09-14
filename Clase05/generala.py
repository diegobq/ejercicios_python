# generala.py
# Ejercicio 5.2: Generala no necesariamente servida
import random
from collections import Counter

def tirar():
    total_tiradas = 3
    total_dados = 5
    repeticion_en_cara = (0, 0)
    repeticiones = Counter()
    tirada = [0] * total_dados
    cara_elegida = 0

    # vamos a lanzar más de una vez...
    for nro_mano in range(total_tiradas):
        # la primera vez tiramos todos los dados...
        # en las siguientes tiramos todos menos las repeticiones de la cara elegida
        dados_a_tirar = total_dados - repeticiones[cara_elegida]
            
        for nro_tirada in range(dados_a_tirar):
            tiro = random.randint(1,6)
            if cara_elegida == 0 or cara_elegida == tiro:
                repeticiones[tiro] += 1
        if cara_elegida == 0:
            repeticion_en_cara = repeticiones.most_common(1)[0]
            cara_elegida = repeticion_en_cara[0]
        i = 0
        while i < repeticiones[cara_elegida]:
            tirada[i] = cara_elegida
            i += 1

    return tirada

def es_generala(tirada):
    i = 1
    repeticiones = 1
    while i < len(tirada) and tirada[i] == tirada[0]:
        repeticiones += 1
        i += 1
    
    return repeticiones == len(tirada)

def prob_generala(N):
    G = sum([es_generala(tirar()) for i in range(N)])
    prob = G/N
    return prob
