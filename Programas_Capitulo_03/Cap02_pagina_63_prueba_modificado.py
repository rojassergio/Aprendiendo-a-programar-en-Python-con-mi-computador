# coding: utf-8
import numpy as np
a = 1.0
b = 4.0
c = - 4.0
print('Los coeficientes son a = '),
print(a),
print(', b = '),
print(b),
print(' y c = '),
print(c)
x1 = (-b + np.sqrt(b**2-4*a*c))/(2*a)
print('La raiz x1 = '),
print(x1)
test_x1 = a*x1**2 + b*x1 + c
print('La raiz x1 en a*x1**2 + b*x1 + c = '),
print(test_x1)
x2 = (-b - np.sqrt(b**2-4*a*c))/(2*a)
print('La raiz x2 = '),
print(x2)
test_x2 = a*x2**2 + b*x2 + c
print('La raiz x2 en a*x2**2 + b*x2 + c = '),
print(test_x2)
sumaX1X2ybSobrea = (x1+x2) + b/a
print('(x1+x2) + b/a = '),
print(sumaX1X2ybSobrea)
ProductoRaicesMenosCsobreA = x1*x2 - c/a
print('x1*x2 - c/a = '),
print(ProductoRaicesMenosCsobreA)
