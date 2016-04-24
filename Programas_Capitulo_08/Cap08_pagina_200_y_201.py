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
def f(z):
    return z*z - 1
 
#In [2]: 
maxitera = 40

#In [3]: 
z0 = -1.3 + 0.5j

#In [4]: 
i=0

#In [5]: 
while i < maxitera:
        z0 = f(z0)
        i = i + 1
        
#In [6]: 
print(abs(z0))

#In [7]: 
z0 = 0.8 +0.2j

#In [8]: 
i=0

#In [9]: 
while i < maxitera:
        z0 = f(z0)
        i = i + 1

#In [10]: 
print(abs(z0))

#In [11]: 
z0 = 0.1 - 0.2j

#In [12]: 
i=0

#In [13]: 
while i < maxitera:
       z0 = f(z0)
       i = i + 1
 
#In [14]: 
print(abs(z0))

#In [15]: 
z0 = 0.1 - 0.2j

#In [16]: 
i=0

#In [17]: 
while i < maxitera:
      print('i = {0} ; z0 = ({1: 5.3f}, {2: 5.3f})'.format(i,z0.real,z0.imag))
      z0 = f(z0)
      i = i + 1

