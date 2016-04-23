'''
@author: Sergio Rojas
@contact: rr.sergio@gmail.com
--------------------------
Contenido bajo
 Atribución-NoComercial-CompartirIgual 3.0 Venezuela (CC BY-NC-SA 3.0 VE)
 http://creativecommons.org/licenses/by-nc-sa/3.0/ve/

Creado en abril 21, 2016
'''

def f(x):
   return (x**2 + 3)

def g(x):
   return (6.0*x**2 + 5.0*x + 8.0)

x = 0

y = g(x)

print(y)

print(f(y))

print(f(g(x)))

print(f(g(7.0)))

print(g(f(0)))


