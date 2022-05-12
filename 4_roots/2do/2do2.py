#
# generate a function to produce points 
#
# -*- coding: utf-8 -*-
"""
Created on  Wed May 10 10:11:15 2022
@author: naran
"""
import sys
import matplotlib.pyplot as plt
import numpy as np

secuencia = (x/10 for x in range(1, 100))
for x in secuencia:
    px = np.array([5, x])

py = np.array([1, 30])
plt.plot(px, py)
plt.show()

plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
