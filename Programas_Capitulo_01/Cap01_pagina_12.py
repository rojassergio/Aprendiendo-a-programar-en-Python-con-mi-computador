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

a, b, c, d, e, f, x, y = symbols ('a b c d e f x y ')

eqs = (a*x + b*y - e, c*x + d*y -f)

res = solve(eqs , x, y)

print(res)
