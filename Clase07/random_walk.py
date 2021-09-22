# Ejercicio 7.12: Caminatas al azar

import numpy as np
import matplotlib.pyplot as plt

def randomwalk(largo):
    '''
    Retorna una secuencia aleatoria de pasos
    Pre: largo debe ser mayor que cero

    Parameters
    ----------
    largo : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    '''
    pasos = np.random.randint(-1,2,largo)
    return pasos.cumsum()

def main():
    num_trayectorias = 12
    N = 100000

    figure = plt.figure()

    ax = figure.add_subplot(2, 1, 1)
    ax.set_title(f'{num_trayectorias} Caminatas al azar', {'fontsize': 10})

    max_distancia = None
    trayectoria_mayor = []

    min_distancia = None
    trayectoria_menor = []

    for i in range(num_trayectorias):
        trayectoria = randomwalk(N)

        distancia = trayectoria[-1]
        if max_distancia == None or distancia > max_distancia:
            max_distancia = distancia
            trayectoria_mayor = trayectoria
        if min_distancia == None or distancia < min_distancia:
            min_distancia = distancia
            trayectoria_menor = trayectoria

        ax.plot(trayectoria)

    ax1 = figure.add_subplot(2, 2, 3)
    ax1.set_title('La caminata que más se aleja', {'fontsize': 7})
    ax1.plot(trayectoria_mayor)

    ax2 = figure.add_subplot(2, 2, 4)
    ax2.set_title('La caminata que menos se aleja', {'fontsize': 7})
    ax2.plot(trayectoria_menor)

    # Set common labels
    figure.text(0.5, 0.04, 'tiempo', ha='center', va='center')
    figure.text(0.06, 0.5, 'distancia al origen', ha='center', va='center', rotation='vertical')

    plt.show()

main()

