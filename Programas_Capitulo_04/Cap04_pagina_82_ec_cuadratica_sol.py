'''
@author: Sergio Rojas
@contact: rr.sergio@gmail.com
--------------------------
Contenido bajo
 Atribución-NoComercial-CompartirIgual 3.0 Venezuela (CC BY-NC-SA 3.0 VE)
 http://creativecommons.org/licenses/by-nc-sa/3.0/ve/

Creado en abril 21, 2016
'''

mensaje = \
"""
-----
 Este programa genera las soluciones de la ecuacion
 cuadratica:
      a*X**2 + b*X + c = 0
 El usuario debe modificar los valores de las constantes a, b y c
 de manera que correspondan al problema que resuelve.

 version del programa: 1
-----
"""

import numpy as np
print(mensaje)
a = 1.0e-10
a = 1.0e-7 # smaller gives one root wrong
b = 62.10
a = 1.0
b = 10000.0
c = 1.0
print(' Los valores de las constantes son: a = '),
print(a), 
print('; b = '), 
print(b), 
print('; c = '), 
print(c)
if (a != 0):
	D = b**2 - 4.0*a*c
	Denominador = 2.0*a
	if (D >= 0):
	    SqrtD = np.sqrt(D)
	    x1= (-b + SqrtD )/Denominador
	    x2= (-b - SqrtD )/Denominador
            print("   ")
	    print("Las raices son reales:")
	    print(" x1 = "),
            print(x1)
	    print(" x2 = "),
            print(x2)
	    print('a*x1**2 + b*x1 + c = '),
	    print(a*x1**2 + b*x1 + c)
	    print('a*x2**2 + b*x2 + c = '),
	    print(a*x2**2 + b*x2 + c)
	    print('(x1 + x2) + b/a = '),
	    print((x1+x2) + float(b)/float(a))
	    print('  x1*x2   - c/a = '),
	    print(x1*x2 - float(c)/float(a))
	else:
	    SqrtD = np.sqrt(D + 0j)
	    x1= (-b + SqrtD )/Denominador
	    x2= (-b - SqrtD )/Denominador
            print("   ")
	    print("Las raices son complejas:")
	    print(" x1 = "),
            print(x1)
	    print(" x2 = "),
            print(x2)
	    print('a*x1**2 + b*x1 + c = '),
	    print(a*x1**2 + b*x1 + c)
	    print('a*x2**2 + b*x2 + c = '),
	    print(a*x2**2 + b*x2 + c)
	    print('(x1 + x2) + b/a = '),
	    print((x1+x2) + float(b)/float(a))
	    print('  x1*x2   - c/a = '),
	    print(x1*x2 - float(c)/float(a))
else:
    print("   ")
    print("La constante del termino cuadratico 'a' no puede ser cero")
    print("Realice la correcion respectiva y ejecute el programa nuevamente.")
