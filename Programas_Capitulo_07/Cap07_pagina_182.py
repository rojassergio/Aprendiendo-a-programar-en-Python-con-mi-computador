'''
@author: Sergio Rojas
@contact: rr.sergio@gmail.com
--------------------------
Contenido bajo
 Atribución-NoComercial-CompartirIgual 3.0 Venezuela (CC BY-NC-SA 3.0 VE)
 http://creativecommons.org/licenses/by-nc-sa/3.0/ve/

Creado en abril 23, 2016
'''

#In [1]: 
import numpy as np

#In [2]: 
x = [1,2,3,4,5,6,7,8,9]

#In [3]: 
nfilas = 3

#In [4]: 
ncolums = 3

#In [5]: 
print(x)

#In [6]: 
X = np.array(x).reshape(nfilas , ncolums)

#In [7]: 
print(X)

#In [8]: 
print(type(x))

#In [9]: 
print(type(X))

#In [10]: 
u = np.array(x)

#In [11]: 
print(u)

#In [12]: 
print(type(u))

#In [13]: 
U = u.reshape(nfilas , ncolums)

#In [14]: 
print(U)

#In [15]: 
print(U-X)

#In [16]: 
print(U**2)

#In [17]: 
print(x**2)

#In [18]: 

