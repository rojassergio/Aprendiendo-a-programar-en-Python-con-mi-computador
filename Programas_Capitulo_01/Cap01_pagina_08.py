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

m11 , m12 , m13 , m14 = symbols (" m11 , m12 , m13 , m14 ")
m21 , m22 , m23 , m24 = symbols (" m21 , m22 , m23 , m24 ")
m31 , m32 , m33 , m34 = symbols (" m31 , m32 , m33 , m34 ")
m41 , m42 , m43 , m44 = symbols (" m41 , m42 , m43 , m44 ")

M = Matrix ([[ m11 , m12 , m13 , m14], \
             [ m21 , m22 , m23 , m24], \
             [ m31 , m32 , m33 , m34], \
             [ m41 , m42 , m43 , m44 ]])
print(M)

print(M.det())
