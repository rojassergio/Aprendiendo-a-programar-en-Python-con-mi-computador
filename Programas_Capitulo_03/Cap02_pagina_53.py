'''
@author: Sergio Rojas
@contact: rr.sergio@gmail.com
--------------------------
Contenido bajo
 Atribución-NoComercial-CompartirIgual 3.0 Venezuela (CC BY-NC-SA 3.0 VE)
 http://creativecommons.org/licenses/by-nc-sa/3.0/ve/

Creado en abril 21, 2016
'''

#pagina 51-52
# ---------
import numpy as np
print(( -(2.5) + np. sqrt ( (2.5)**2 - 4*(3.2)*( -0.3) ) )/(2*(3.2)))
print(( -(2.5) - np. sqrt ( (2.5)**2 - 4*(3.2)*( -0.3) ) )/(2*(3.2)))

a =3.2
b =2.5
c= -0.3

x1 = ( -b + np. sqrt (b **2 - 4*a*c) )/(2* a)

print(x1)

x2 = ( -b - np. sqrt (b **2 - 4*a*c) )/(2* a)

print(x2)

sol1 = a*x1 **2 + b*x1 + c
print(sol1)

sol2 = a*x2 **2 + b*x2 + c
print(sol2)

# pagina 53
# ---------
x =3.2
y =2.5
z= -0.3

a=( -y + np. sqrt (y**2 - 4*x*z) )/(2* x)
print(a)

b=( -y - np. sqrt (y**2 - 4*x*z) )/(2* x)
print(b)

