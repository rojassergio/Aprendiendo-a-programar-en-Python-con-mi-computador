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
 El usuario debe ingresar los valores de las constantes a, b y c
 que correspondan al problema que resuelve.

 version del programa: 2
-----
"""
def myprint(str0, a, b, c, x1, x2):
    """
    -----
      Esta funcion muestra en pantalla del computador resultados
      asociados a las soluciones de la ecuacion cuadratica:
            a*X**2 + b*X + c = 0

      version de la funcion: 1
    -----
    """
    print("\n Con valores a = {0}, b = {1} y c = {2:<}".format(a, b, c))
    str1 = 'x1 ='
    str2 = 'x2 ='
    print(" {0:<10} \n  {1:>10} {2} \
                    \n  {3:>10} {4}  ".format(str0, str1, x1, str2, x2))
    str1 = 'a*x1**2 + b*x1 + c = '
    str2 = 'a*x2**2 + b*x2 + c = '
    v1   = a*x1**2 + b*x1 + c
    v2   = a*x2**2 + b*x2 + c
    print("    \n  {0:>30} {1} \
               \n  {2:>30} {3}  ".format(str1, v1, str2, v2))
    str1 = '(x1 + x2) + b/a = '
    str2 = '  x1*x2  -  c/a = '
    v1   = (x1+x2) + float(b)/float(a)
    v2   = x1*x2 - float(c)/float(a)
    print("    \n  {0:>30} {1} \
               \n  {2:>30} {3}  ".format(str1, v1, str2, v2))

def SolEcCuadratica(a, b, c):
    """
    -----
      Esta funcion genera las soluciones de la ecuacion
      cuadratica:
            a*X**2 + b*X + c = 0

      version de la funcion: 1
    -----
    """
    import numpy as np
    if (a != 0):
	D = b**2 - 4.0*a*c
	Denominador = 2.0*a
	if (D >= 0):
	    SqrtD = np.sqrt(D)
            if ( b >= 0 ):
	       x1= (-b - SqrtD )/Denominador
	       x2= - (2.0*c)/( b + SqrtD )
            else:
	       x1= (-b + SqrtD )/Denominador
	       x2= - (2.0*c)/( b - SqrtD )
	    myprint("Las raices son reales:", a, b, c, x1, x2)
	else:
	    SqrtD = np.sqrt(D + 0j)
	    x1= (-b + SqrtD )/Denominador
	    x2= (-b - SqrtD )/Denominador
	    myprint("Las raices son complejas:", a, b, c, x1, x2)
        return x1, x2
    else:
      print("   ")
      print("La constante del termino cuadratico 'a' no puede ser cero")
      print("Realice la correcion respectiva y ejecute el programa nuevamente.")
      return None

import numpy as np
print(mensaje)
a = 1.0e-7 # smaller gives one root wrong
a = 1.0e-15
b = 62.10
a = 0
a = 1.0
b = 10000.0
c = 1.0
b = 1.0

x1, x2 = SolEcCuadratica(a, b, c)
