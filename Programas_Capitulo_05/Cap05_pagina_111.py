'''
@author: Sergio Rojas
@contact: rr.sergio@gmail.com
--------------------------
Contenido bajo
 Atribución-NoComercial-CompartirIgual 3.0 Venezuela (CC BY-NC-SA 3.0 VE)
 http://creativecommons.org/licenses/by-nc-sa/3.0/ve/

Creado en abril 21, 2016
'''

mostrar = "Valor 1: {0}; Valor 2: {1}".format(14,231.2015)

print(mostrar)

mostrar = "Valor 1: {0:4d}; Valor 2: {1:7.2f}".format(14,231.2015)

print(mostrar)

mostrar = "Valor 1: {1:7.3f}; Valor 2: {0:7.2f}".format(14,231.2015)

print(mostrar)


def myprint(a, b, c, x1, x2):
            str1 = 'x1 ='
            str2 = 'x2 ='
	    print("\n Las raices son reales: \
                         \n  {0:>10} {1} \
                         \n  {2:>10} {3}  ".format(str1, x1, str2, x2))
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

