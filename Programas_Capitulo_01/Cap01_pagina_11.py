'''
@author: Sergio Rojas
@contact: rr.sergio@gmail.com
--------------------------
Contenido bajo
 Atribución-NoComercial-CompartirIgual 3.0 Venezuela (CC BY-NC-SA 3.0 VE)
 http://creativecommons.org/licenses/by-nc-sa/3.0/ve/

Creado en abril 18, 2016
'''

from sympy import *

x, y = symbols ('x y ')

a = 3.5; b =1.7; c =12.3; d=- 23.4; e= -2.5; f =3.6

eqs = (a*x + b*y - e, c*x + d*y -f)

res = solve (eqs , x, y)

print(res)
