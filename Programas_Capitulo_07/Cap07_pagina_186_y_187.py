'''
@author: Sergio Rojas
@contact: rr.sergio@gmail.com
--------------------------
Contenido bajo
 Atribución-NoComercial-CompartirIgual 3.0 Venezuela (CC BY-NC-SA 3.0 VE)
 http://creativecommons.org/licenses/by-nc-sa/3.0/ve/

Creado en abril 23, 2016
'''

# Pagina 186
#In [1]: 
import numpy as np

#In [2]: 
x = [0.0, 1.5, 3.0, 4.5, 6.0, ]

#In [3]: 
y = [0.0, 0.86, 1.71, 2.57, 3.43, 4.29, 5.14, 6.0]

#In [4]: 
X, Y  = np.meshgrid(x,y)

#In [5]: 
print(X)

#In [6]: 
print(Y)

#In [7]: 
print(np.shape(X))

#In [8]: 
print(np.shape(Y))

# Pagina 187
#-----------
#In [9]: 
Z = 4*X**2 + Y**2

#In [10]: 
print(Z)

#In [11]: 
print(np.shape(Z))

#In [12]: 
Z = X*Y

#In [13]: 
print(Z)

#In [14]: 

