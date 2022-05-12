#
# refer to PPT file
# for exercise
# obtener raiz e2-x -7x = 0

# -*- coding: utf-8 -*-
"""
Created on Sat May  7 22:15:32 2022
@author: naran
"""
import matplotlib.pyplot as plt
from math import exp


def fn(x):
    return exp(2-x)-7*(x)


def f2(x):
    return -exp(2-x)/-7


x0 = 1.055

x1 = -exp(2-x0)/-7
print("x1 = ", x1)
x2 = -exp(2-x1)/-7
print('x2 = ', x2)
x3 = -exp(2-x2)/-7
print("x3 = ", x3)
x4 = -exp(2-x3)/-7
print("x4 = ", x4)
x5 = -exp(2-x4)/-7
print("x5 = ", x5)
print("La raiz de e^(2-x)-7x=0 es: ", x5)

#xplt = [-2, -1, 0, 1, 2]
#yplt = [-61.59, -27.08, -14.38, -9.71, 8]
#print(plt.scatter(xplt, yplt))
