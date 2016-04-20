'''
@author: Sergio Rojas
@contact: rr.sergio@gmail.com
--------------------------
Contenido bajo
 Atribución-NoComercial-CompartirIgual 3.0 Venezuela (CC BY-NC-SA 3.0 VE)
 http://creativecommons.org/licenses/by-nc-sa/3.0/ve/

Creado en abril 19, 2016
'''

A =0.0254
B =9788.0
print(((A+B )**2 -2* A*B-B **2)/ A**2)
ER=abs(1 -1.0000241431738204)
print(ER)

A =9788.0
B =0.0254
print(((A+B )**2 -2* A*B-B **2)/ A**2)
ER=abs(1 -1.0000000000000002)
print(ER)

