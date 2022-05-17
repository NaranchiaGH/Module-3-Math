# -*- coding: utf-8 -*-
"""
Created on Mon May 9 22:12:38 2022

@author: naran
"""
# Estimar el polinomio interpolante donde, (-1,3), (0,-7), (4,7) y (5,11)
# utilizar libreria numpy
import numpy as np
from scipy.interpolate import lagrange

x = np.array([-1, 0, 4, 5])

y = np.array([3, -7, 7, 11])

print("El polinomio interpolante es: \n" + str(lagrange(x, y)))
