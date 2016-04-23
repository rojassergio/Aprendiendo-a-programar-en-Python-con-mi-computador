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

def f(x, a=2.5, b = np.sqrt(3), c = 3.2):
    return a*x**2 + b*x + c

print(f(0))

print(f(1))

print(f(np.sqrt(7)))

print(f(0, c = 9))

print(f(1, c=9, a=0, b=1))

print(f(1, c=9, a=0))

print(f(c=9, a=0, x=1))

print(f(c=9, a=0, x=1, b=6.5))

print("\t EJECUTAR LAS SIGUIENTES 2 instrucciones desde Ipython")
print("\t despues de ejecutar: %run Cap05_pagina_105.py")
print("\t f(9, a=0, 1, b=6.5)")
print("\t f(9, a=0, 1, 6.5)")

print(f(9, 0, 1, 6.5))

