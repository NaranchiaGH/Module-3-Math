#
# generate a function to produce points 
# to be used as x-axis
# 
# INPUT
# -> a initial point
# -> b final point
# -> c increment
#
# OUTPUT
# <- list of points
#
# for instance for this range [1,10,.1]
# it will produce 100 points
# [1.0, 1.1, ... , 9.9, 10]
import numpy as np
import matplotlib.pyplot as plt

a = float(input("Ingresa el punto inicial: "))
b = float(input("Ingresa el punto final: "))
c = float(input("Ingresa el incremento: "))
x = np.arange(a, b, c)
y = [Xn**1 for Xn in x]

plt.title("produce points")
plt.scatter(x, y, edgecolors=('red'))
plt.show()

# rango x - axis
# plt.axis(xmin=i_point, xmax=f_point)

