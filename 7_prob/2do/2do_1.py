"""
Probabilidades
Brujula
"""
# 2do_1
from random import choice


def brujula():
    return choice(['norte', 'sur', 'este', 'oeste'])


for i in range(10):
    print("La brujula apunta hacia el,", brujula())
