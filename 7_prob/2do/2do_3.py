"""
Probabilidades
# select a distribution from random
# produce random numbers on such a distribution
#
# zeeAlso
# en.wikipedia.org/wiki/Probability_distribution
#
# 2do_3
# betavariate and gaussian distribution
"""
import random
import matplotlib.pyplot as plt

# betavariate
# random.betavariate(alpha, beta)
nums = []
bajo = 10
alto = 100
mode = 20
for i in range(100):
    temp = random.betavariate(5, 10)
    nums.append(temp)
plt.plot(nums)
plt.show()

# Gauss
# almacenando los números aleatorios en una lista
nums = []
mu = 100  # media
sigma = 50  # Desviacion estandar

# Generando aleatorios
for i in range(10000):
    temp = random.gauss(mu, sigma)
    nums.append(temp)

plt.hist(nums, bins=200)
plt.show()
