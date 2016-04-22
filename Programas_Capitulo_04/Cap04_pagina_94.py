'''
@author: Sergio Rojas
@contact: rr.sergio@gmail.com
--------------------------
Contenido bajo
 Atribución-NoComercial-CompartirIgual 3.0 Venezuela (CC BY-NC-SA 3.0 VE)
 http://creativecommons.org/licenses/by-nc-sa/3.0/ve/

Creado en abril 21, 2016
'''

a = 0j
print(type(a))
print(isinstance(a,complex))
print(a != 0)
print(a == 0)
b = 1.
c = 1.
escomplejo = isinstance( (a + b + c), complex)
print(escomplejo)
print((not (escomplejo)))
print((a != 0) and (not (escomplejo)))

a = 1.0
escomplejo = isinstance( (a + b + c), complex)
print(escomplejo)
print((a != 0) and (not (escomplejo)))
