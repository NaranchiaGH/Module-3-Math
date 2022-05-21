"""
Probabilidades
#
# select a distribution from numpy
# produce random numbers on such a distribution
# 
# zeeAlso
# en.wikipedia.org/wiki/Probability_distribution
#
# 2do_4
# poisson distribution
"""
import numpy as np
import matplotlib.pyplot as plt

s = np.random.poisson(5, 10000)  # generando randoms

# matplotlib.pyplot.hist
conteo, bins, dens = plt.hist(s, 14, density=True)  # Utilizo el plot hist y sus parametros
plt.show()
