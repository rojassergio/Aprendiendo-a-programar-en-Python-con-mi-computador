'''
@author: Sergio Rojas
@contact: rr.sergio@gmail.com
--------------------------
Contenido bajo
 Atribución-NoComercial-CompartirIgual 3.0 Venezuela (CC BY-NC-SA 3.0 VE)
 http://creativecommons.org/licenses/by-nc-sa/3.0/ve/

Creado en abril 21, 2016
'''

from sympy import *
X, a, b, c = symbols ('X a b c ')
X = (-b + sqrt (b**2 - 4*a*c ))/(2* a)
print(X)
print(a*X**2 + b*X + c)
print(simplify ( a*X**2 + b*X + c ))
print(expand ( a*X**2 + b*X + c ))

print(simplify ( a*X**2 + b*X + c ) == 0)

print(expand( a*X**2 + b*X + c ) == 0)

res = a*X**2 + b*X + c
print(res)

print(res == a*X**2 + b*X + c)

sol = simplify (res) == 0
print(sol)

