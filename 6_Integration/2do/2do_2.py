# 2do_2
# dado (7^(-x))+3 cuando a = -1 y b = 2
# minimo 2 metodos a elegir


def f(x):
    return (7**(-x))+3


a = -1
b = 2

metodo_1 = f((a+b)/2)*(b-a)
print('Regla del punto medio =', metodo_1)

metodo_2 = ((b-a)/6)*(f(a)+(4*f((a+b)/2)+f(b)))
print('Regla de Simpson =', metodo_2)
