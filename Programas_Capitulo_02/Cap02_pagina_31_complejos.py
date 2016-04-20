'''
@author: Sergio Rojas
@contact: rr.sergio@gmail.com
--------------------------
Contenido bajo
 Atribución-NoComercial-CompartirIgual 3.0 Venezuela (CC BY-NC-SA 3.0 VE)
 http://creativecommons.org/licenses/by-nc-sa/3.0/ve/

Creado en abril 19, 2016
'''

import numpy as np

print(2 + 3j)
print((2+3j) + (2 -3j))
print((2+3j) - (2 -3j))
print((2+3j)*(2 -3j))
print((2+3j)/(2 -3j))
print(np. sqrt (-2 + 0j))
print(np.lib.scimath.sqrt(-2))

from numpy.lib.scimath import sqrt as csqrt

print(csqrt(-2))
