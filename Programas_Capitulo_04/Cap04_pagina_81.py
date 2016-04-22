'''
@author: Sergio Rojas
@contact: rr.sergio@gmail.com
--------------------------
Contenido bajo
 Atribución-NoComercial-CompartirIgual 3.0 Venezuela (CC BY-NC-SA 3.0 VE)
 http://creativecommons.org/licenses/by-nc-sa/3.0/ve/

Creado en abril 21, 2016
'''

print("a" < "b")
print("a" < "z")
print("z" < "Z")
print("metro" < "kilometro")
print("caso" > "casa")

#IF anidados
#----------
x = 1
if (x > 0):
   x=x*3
   if (x > 4):
      y = -1
      x = x + y
   else:
      if (x > 1):
        y = 2
        x = x + y
else:
   y = 3
   x = x + y
print('Despues del bloque if, el valor en x = '),
print(x)

