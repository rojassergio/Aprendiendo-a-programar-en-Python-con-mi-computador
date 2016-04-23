'''
@author: Sergio Rojas
@contact: rr.sergio@gmail.com
--------------------------
Contenido bajo
 Atribución-NoComercial-CompartirIgual 3.0 Venezuela (CC BY-NC-SA 3.0 VE)
 http://creativecommons.org/licenses/by-nc-sa/3.0/ve/

Creado en abril 21, 2016
'''

# In [1]: 
from scipy.optimize import bisect as scibiseccion

#In [2]: 
def f(x):
    return (x**2 + 4.0*x - 4.0) 

#In [3]: 
print(scibiseccion(f, a=-6, b=-4, rtol=1.e-10))

#In [4]: 

