'''
@author: Sergio Rojas
@contact: rr.sergio@gmail.com
--------------------------
Contenido bajo
 Atribución-NoComercial-CompartirIgual 3.0 Venezuela (CC BY-NC-SA 3.0 VE)
 http://creativecommons.org/licenses/by-nc-sa/3.0/ve/

Creado en abril 21, 2016
'''

x = 1
print('Antes del bloque if, el valor en x = '),
print(x)
if (x > 0):
      y = -1
      x = x + y
elif (x > 0.5):
      y = 2
      x = x + y
else:
   y = 3
   x = x + y
print('Despues del bloque if, el valor en x = '),
print(x)

