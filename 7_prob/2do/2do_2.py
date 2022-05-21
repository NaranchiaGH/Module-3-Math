"""
Probabilidades
# produce 10,000 coin flips
# print how many of them were:
# heads
# tails
# 2do_2
"""
from random import choice


def lanzarMoneda():
    return choice(['aguila', 'sello'])


def cara(veces):
    val = {}
    for iteration in range(veces):
        moneda = lanzarMoneda()
        val[moneda] = val.get(moneda, 0) + 1
    return val


print(cara(50))
