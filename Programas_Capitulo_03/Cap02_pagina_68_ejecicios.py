'''
@author: Sergio Rojas
@contact: rr.sergio@gmail.com
--------------------------
Contenido bajo
 Atribución-NoComercial-CompartirIgual 3.0 Venezuela (CC BY-NC-SA 3.0 VE)
 http://creativecommons.org/licenses/by-nc-sa/3.0/ve/

Creado en abril 21, 2016
'''

#Problema 3.4
#------------
x=4
suma = 0
for i in range(x):
    suma = suma + x
print("El cuadrado de"),
print(x),
print(" es "),
print(suma)

#Problema 3.5
#-------------
x=4
x0 = x
repetir = 0
suma = 0
while repetir < x0:
   suma = suma + x
   repetir = repetir + 1
print("El cuadrado de"),
print(x),
print(" es "),
print(suma)


#Problema 3.6
#--------------
x=4
decrecer = x
suma = 0
while decrecer != 0:
  suma = suma + x
  decrecer = decrecer - 1
print("El cuadrado de"),
print(x),
print(" es "),
print(suma)
