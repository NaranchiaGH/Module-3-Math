# 2do_1
# dado 2sen(sqrt(x))-x cuando a = 0 y b = 1.9724
# minimo 2 metodos a elegir

from math import sin
from math import sqrt


def f(x):
    return 2*sin(sqrt(x))-x


a = 0
b = 1.9724

metod_1 = f(a)*(b-a)
print('Regla del rectangulo =', metod_1)

metod_2 = f((a+b)/2)*(b-a)
print('Regla del punto medio =', metod_2)

metod_3 = ((b-a)/2)*(f(a)+f(b))
print('Regla del trapecio =', metod_3)

metod_4 = ((b-a)/6)*(f(a)+(4*f((a+b)/2)+f(b)))
print('Regla de Simpson =', metod_4)
