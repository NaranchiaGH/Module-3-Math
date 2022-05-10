# -*- coding: utf-8 -*-
"""
Created on Sat May  7 22:15:32 2022

@author: naran
"""
import matplotlib.pyplot as plt
from math import exp


def f(x):  # Función
    return exp(2-x)-7*x


def f2(x):  # Derivada
    return -exp(2-x)-7


x0 = 1.5

x1 = x0-f(x0)/f2(x0)
print('x1 = ', x1)

x2 = x1-f(x1)/f2(x1)
print('x2 = ', x2)

x3 = x2-f(x2)/f2(x2)
print('x3 = ', x3, '\n')
print('valor = ', f(x3))
print('La raiz es: ', x3)

xplt = [-2, -1, 0, 1, 2]
yplt = [-61.59, -27.08, -14.38, -9.71, 8]
print(plt.scatter(xplt, yplt))
