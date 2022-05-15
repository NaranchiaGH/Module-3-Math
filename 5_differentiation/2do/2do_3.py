# Diferenciacion numerica / derivacion numerica
# Tarea 2do_2
# f(x) = (sen^(3)2x)/(x^(4)+1) obtener f(2.45)

# Metodo 3: Derivada de primer orden hacia adelante

from math import sin


def f(x):

    return (sin(2*x))**3/((x**4)+1)


x0 = 2.45

h1 = 0.5
v1 = (f(x0+h1/2)-f(x0-h1/2))/h1
print('valor 1 =', v1)

h2 = 0.3
v2 = (f(x0+h2/2)-f(x0-h2/2))/h2
print('valor 2 =', v2)

h3 = 0.0001
v3 = (f(x0+h3/2)-f(x0-h3/2))/h3
print('valor 3 =', v3)

h4 = 0.0000001
v4 = (f(x0+h4/2)-f(x0-h4/2))/h4
print('valor 4 =', v4)

h5 = 0.00000000001
v5 = (f(x0+h5/2)-f(x0-h5/2))/h5
print('valor 5 =', v5)
