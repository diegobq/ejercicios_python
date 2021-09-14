# plotear_temperaturas.py
# Ejercicio 5.9: Empezando a plotear
import numpy as np
import matplotlib.pyplot as plt

def plotear_temperaturas():
    temperaturas = np.load('../Data/temperaturas.npy')
    plt.hist(temperaturas, bins=50)
    plt.show()