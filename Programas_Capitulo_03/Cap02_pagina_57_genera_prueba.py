'''
@author: Sergio Rojas
@contact: rr.sergio@gmail.com
--------------------------
Contenido bajo
 Atribución-NoComercial-CompartirIgual 3.0 Venezuela (CC BY-NC-SA 3.0 VE)
 http://creativecommons.org/licenses/by-nc-sa/3.0/ve/

Creado en abril 21, 2016
'''


$ ipython --pylab
Python 2.7.10 | 64-bit | (default, Oct 21 2015, 12:08:08) 
Type "copyright", "credits" or "license" for more information.

IPython 2.4.1 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.
Using matplotlib backend: Qt4Agg

In [1]: import numpy as np

In [2]: a = 1.0

In [3]: b = 4.0

In [4]: c = - 4.0

In [5]: x1 = (-b + np. sqrt (b**2 -4*a*c ))/(2* a)

In [6]: print (x1)
0.828427124746

In [7]: test_x1 = a*x1 **2 + b*x1 + c

In [8]: print ( test_x1 )
8.881784197e-16

In [9]: x2 = (-b - np. sqrt (b**2 -4*a*c ))/(2* a)

In [10]: print (x2)
-4.82842712475

In [11]: test_x2 = a*x2 **2 + b*x2 + c

In [12]: print ( test_x2 )
0.0

In [13]: sumaX1X2ybSobrea = (x1+x2) + b/a

In [14]: print ( sumaX1X2ybSobrea )
4.4408920985e-16

In [15]: ProductoRaicesMenosCsobreA = x1*x2 - c/a

In [16]: print ( ProductoRaicesMenosCsobreA )
-8.881784197e-16

In [17]: %save prueba.py 1-16
The following commands were written to file `prueba.py`:
import numpy as np
a = 1.0
b = 4.0
c = - 4.0
x1 = (-b + np. sqrt (b**2 -4*a*c ))/(2* a)
print (x1)
test_x1 = a*x1 **2 + b*x1 + c
print ( test_x1 )
x2 = (-b - np. sqrt (b**2 -4*a*c ))/(2* a)
print (x2)
test_x2 = a*x2 **2 + b*x2 + c
print ( test_x2 )
sumaX1X2ybSobrea = (x1+x2) + b/a
print ( sumaX1X2ybSobrea )
ProductoRaicesMenosCsobreA = x1*x2 - c/a
print ( ProductoRaicesMenosCsobreA )

In [18]: %ls -l prueba.py
-rw-rw-r-- 1 srojas srojas 403 Apr 21 15:34 prueba.py

In [19]: %cat prueba.py
# coding: utf-8
import numpy as np
a = 1.0
b = 4.0
c = - 4.0
x1 = (-b + np. sqrt (b**2 -4*a*c ))/(2* a)
print (x1)
test_x1 = a*x1 **2 + b*x1 + c
print ( test_x1 )
x2 = (-b - np. sqrt (b**2 -4*a*c ))/(2* a)
print (x2)
test_x2 = a*x2 **2 + b*x2 + c
print ( test_x2 )
sumaX1X2ybSobrea = (x1+x2) + b/a
print ( sumaX1X2ybSobrea )
ProductoRaicesMenosCsobreA = x1*x2 - c/a
print ( ProductoRaicesMenosCsobreA )

In [20]: %who
ProductoRaicesMenosCsobreA	 a	 b	 c	 sumaX1X2ybSobrea	 test_x1	 test_x2	 x1	 x2	 


In [21]: %reset -f

In [22]: %who
Interactive namespace is empty.

In [23]: print(a)
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-23-c5a4f3535135> in <module>()
----> 1 print(a)

NameError: name 'a' is not defined

In [24]: %run prueba.py
0.828427124746
8.881784197e-16
-4.82842712475
0.0
4.4408920985e-16
-8.881784197e-16

In [25]: %who
ProductoRaicesMenosCsobreA	 a	 b	 c	 np	 sumaX1X2ybSobrea	 test_x1	 test_x2	 x1	 
x2	 

In [26]: ProductoRaicesMenosCsobreA
Out[26]: -8.8817841970012523e-16

In [27]: quit

$ python prueba.py
0.828427124746
8.881784197e-16
-4.82842712475
0.0
4.4408920985e-16
-8.881784197e-16

