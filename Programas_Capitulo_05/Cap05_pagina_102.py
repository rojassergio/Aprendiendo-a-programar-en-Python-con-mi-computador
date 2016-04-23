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

# whos # solo funciona en Ipython
print(globals().keys()) # Igual funciona en Ipython

def f(x):
    return ( 2.5*x**2 + np.sqrt(3)*x + 3.2 )

# whos # solo funciona en Ipython
print(globals().keys()) # Igual funciona en Ipython

print(f(0))

print(f(1))

print(f(np. sqrt (7)))

f = 9

print(f(9))

