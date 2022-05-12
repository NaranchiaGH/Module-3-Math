from cmath import sin
import math

print("1.- Evaluar la funcion y = sin(2x) en x = 1.3")
print("2.- Evaluar la funcion y = e^(1-2x) en x = -0.45", "\n")

# Función y = sin(2x) para x = 1.3
y0 = sin(2*1.3)
print("El resultado para y = sin(2x) en x = 1.3 es:", "\n", "Res =", y0)
print()

# Función y = e^(1-2x) en x = -0.45
y1 = math.exp(1-2*(-0.45))
print("El resultado para y = e^(1-2x) en x = -0.45 es:", "\n", "Res =", y1)
print()
