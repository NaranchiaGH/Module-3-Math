import math

# El semiperímetro de un triángulo isósceles es la mitad de la suma de la longitud de todos los lados
s = (8 + 16 + 14) * (1 / 2)
print(s)

Sa = 8  # Semiperimetro lado a
Sb = 16  # Semiperimetro lado b
Sc = 14  # Semiperimetro lado c

# Formula =
# Inradius = sqrt((Semiperímetro-Lado a)*(Semiperímetro-Lado B)*(Semiperímetro-Lado C)/Semiperímetro)

r = math.sqrt(s * (s - Sa) * (s - Sb) * (s - Sc)) / s
print(r)
