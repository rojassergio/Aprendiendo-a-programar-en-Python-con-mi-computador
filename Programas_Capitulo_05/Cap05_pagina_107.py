'''
@author: Sergio Rojas
@contact: rr.sergio@gmail.com
--------------------------
Contenido bajo
 Atribución-NoComercial-CompartirIgual 3.0 Venezuela (CC BY-NC-SA 3.0 VE)
 http://creativecommons.org/licenses/by-nc-sa/3.0/ve/

Creado en abril 21, 2016
'''

x = 'abc'

y = -2.0

def f(x):
    x = x + 1.0
    z = x + 1.0
    print('Dentro de f(x), las variables tiene valores: x = '),
    print(x),
    print('; y = '),
    print(y),
    print(' y z = '),
    print(z)
    return x

print(x)

print(y)

y = f(2)

print(x)

print(y)

x = 5.1

y = f(x)

print(y)

print(z)
