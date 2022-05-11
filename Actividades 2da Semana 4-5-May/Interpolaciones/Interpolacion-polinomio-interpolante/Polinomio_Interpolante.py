# -*- coding: utf-8 -*-
"""
Created on Mon May 9 22:12:38 2022

@author: naran
"""
# Estimar el polinomio interpolante donde, (-1,3), (0,-7), (4,7) y (5,11)

p1 = (-1, 3)
p2 = (0, -7)
p3 = (4, 7)
p4 = (5, 11)
x = float(input("Ingresa el valor de X: "))


def fn(x, p1, p2, p3, p4):
    l1 = (((x-p2[0])*(x-p3[0])*(x-p4[0]))
         / ((p1[0]-p2[0])*(p1[0]-p3[0])*(p1[0]-p4[0])))*(p1[1])
    l2 = (((x-p1[0])*(x-p3[0])*(x-p4[0]))
         / ((p2[0]-p1[0])*(p2[0]-p3[0])*(p2[0]-p4[0])))*(p2[1])
    l3 = (((x-p1[0])*(x-p2[0])*(x-p4[0]))
         / ((p3[0]-p1[0])*(p3[0]-p2[0])*(p3[0]-p4[0])))*(p3[1])
    l4 = (((x-p1[0])*(x-p2[0])*(x-p3[0]))
         / ((p4[0]-p1[0])*(p4[0]-p2[0])*(p4[0]-p3[0])))*(p4[1])
    return l1+l2+l3+l4


print("El valor de y en x =", x, "es:", fn(x, p1, p2, p3, p4))

