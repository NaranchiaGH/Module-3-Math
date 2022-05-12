#
# radious of circle inscribed in a triangle
# place here your solution code
#
#2do

import math

# Valores que ingrese para el ejemplo
# lados a , b , c = (10, 14, 12)
# lado C no puede ser mayor a la suma del lado a y b
# Formula:
# Inradius = sqrt((Semiperímetro-Lado a)*(Semiperímetro-Lado B)*(Semiperímetro-Lado C)/Semiperímetro)


a = float(input("Ingrese el lado a: "))
b = float(input("Ingrese el lado b: "))
c = float(input("Ingrese el lado c: "))

condition = a + b

if(c < condition):
    s = ((a + b + c) * (1 / 2))
    print("El semiperimetro es = ", s)
    r = math.sqrt(s * (s - a) * (s - b) * (s - c)) / s
    print("El radio de la circunferencia inscrita en un triangulo es =", r, "\n")
else:
    print("Error el lado C es mayor a la suma de los otros")
