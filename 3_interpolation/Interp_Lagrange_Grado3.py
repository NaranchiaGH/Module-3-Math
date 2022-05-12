# Interpolación de Lagrange
# Polinomio interpolador de Lagrange grado N=3
# Estimar valor de y, cuando x = 7.7
# (-2,4), (-1,-2), (3,5) y (4.3,11)

x = 7.7; x0 = -2; x1 = -1; x2 = 3; x3 = 4.3
y0 = 4; y1 = -2; y2 = 5; y3 = 11

b0 = ((x-x1)/(x0-x1)*(x-x2)/(x0-x2)*(x-x3)/(x0-x3) * y0)
b1 = ((x-x0)/(x1-x0)*(x-x2)/(x1-x2)*(x-x3)/(x1-x3) * y1)
b2 = ((x-x0)/(x2-x0)*(x-x1)/(x2-x1)*(x-x3)/(x2-x3) * y2)
b3 = ((x-x0)/(x3-x0)*(x-x1)/(x3-x1)*(x-x2)/(x3-x2) * y3)

y = b0 + b1 + b2 + b3
print("El valor de y, cuando x = 7.7 es: ", y)
