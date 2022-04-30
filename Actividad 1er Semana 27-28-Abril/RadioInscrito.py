import math

# Valores que ingrese para el ejemplo
# lado a = 10
# lado b = 14
# lado c = 12 No puede ser mayor a la suma del lado a y b

a = int (input ('Ingrese el lado a: '))
b = int (input ('Ingrese el lado b: '))
c = int (input ('Ingrese el lado c: '))

# El semiperímetro es la mitad de la suma de la longitud de todos los lados
s = (a + b + c) * (1 / 2)
print("El semiperimetro es = ",s)

# Formula =
# Inradius = sqrt((Semiperímetro-Lado a)*(Semiperímetro-Lado B)*(Semiperímetro-Lado C)/Semiperímetro)

r = math.sqrt (s * (s - a) * (s - b) * (s - c)) / s
print("El radio de la circunferencia inscrita en un triangulo es =",r)
