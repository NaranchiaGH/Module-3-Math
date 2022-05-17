# 2do_1
# dado 2sen(sqrt(x))-x cuando a = 0 y b = 1.9724
# minimo 2 metodos a elegir

from math import sin
from math import sqrt


def f(x):
    return 2*sin(sqrt(x))-x


a = 0
b = 1.9724
metodo_1 = ((b-a)/6)*(f(a)+(4*f((a+b)/2)+f(b)))
print('Regla de Simpson =', metodo_1)

metodo_2 = f((a+b)/2)*(b-a)
print('Regla del punto medio =', metodo_2)

metodo_3 = ((b-a)/2)*(f(a)+f(b))
print('Regla del trapecio =', metodo_3)
