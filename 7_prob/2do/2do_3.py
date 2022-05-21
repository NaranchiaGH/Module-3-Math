"""
Probabilidades
# select a distribution from random
# produce random numbers on such a distribution
#
# zeeAlso
# en.wikipedia.org/wiki/Probability_distribution
#
# 2do_3
# gaussian distribution
"""
import random
import matplotlib.pyplot as plt

# almacenando los números aleatorios en una lista
nums = []
mu = 100  # media
sigma = 50  # Desviacion estandar

for i in range(10000):
    temp = random.gauss(mu, sigma)
    nums.append(temp)

plt.hist(nums, bins=200)
plt.show()
