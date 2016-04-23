'''
@author: Sergio Rojas
@contact: rr.sergio@gmail.com
--------------------------
Contenido bajo
 Atribución-NoComercial-CompartirIgual 3.0 Venezuela (CC BY-NC-SA 3.0 VE)
 http://creativecommons.org/licenses/by-nc-sa/3.0/ve/

Creado en abril 21, 2016
'''

import numpy as np

def hacer_f(a, b, c):
    def f(x):
        return a*x**2 + b*x + c
    return f

f = hacer_f(2.5, np.sqrt(3), 3.2)

print(f(0))

print(f(1))

print(f(np.sqrt(7)))

try:
  f(0, c = 9)
except TypeError:
  print("TypeError: f() got an unexpected keyword argument 'c'")
print("\t EJECUTAR LA SIGUIENTE instruccion desde Ipython")
print("\t despues de ejecutar: %run Cap05_pagina_106.py")
print("\t f(0, c = 9)")

f = hacer_f(c=9, a=0, b=1)

print(f(1))

g = hacer_f(c=9, a=0, b=1)

print(g(1))

