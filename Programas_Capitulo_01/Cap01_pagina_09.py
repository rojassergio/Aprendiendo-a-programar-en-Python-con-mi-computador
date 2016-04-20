'''
@author: Sergio Rojas
@contact: rr.sergio@gmail.com
--------------------------
Contenido bajo
 Atribución-NoComercial-CompartirIgual 3.0 Venezuela (CC BY-NC-SA 3.0 VE)
 http://creativecommons.org/licenses/by-nc-sa/3.0/ve/

Creado en abril 18, 2016
'''

import numpy as np
from scipy import linalg
A = np. array ([[3.5 , 1.7] ,[12.3 , -23.4]])
print(A)
B = np. array ([- 2.5 , 3.6])
print(B)

C= linalg.solve(A,B)
print( C )

from scipy import linalg as alg

C= alg.solve (A,B)
print(C)

