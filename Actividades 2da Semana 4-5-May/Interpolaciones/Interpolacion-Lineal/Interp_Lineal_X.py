# Interpolation Lineal
# (-4, -2) y (1, 5) estimar valor para x cuando y = 3.7
x0 = -4; x1 = 1
y = 3.7; y0 = -2; y1 = 5

x = ((x1 - x0) / (y1 - y0) * (y - y0) + x0)
print("El valor para x cuando y = 3.7 es: ", x)
