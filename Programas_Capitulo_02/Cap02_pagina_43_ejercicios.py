'''
@author: Sergio Rojas
@contact: rr.sergio@gmail.com
--------------------------
Contenido bajo
 Atribución-NoComercial-CompartirIgual 3.0 Venezuela (CC BY-NC-SA 3.0 VE)
 http://creativecommons.org/licenses/by-nc-sa/3.0/ve/

Creado en abril 19, 2016
'''

# Problema 2.1
v0 = 5
g = 9.81
t = 0.6
y = v0*t - 0.5*g*t**2
print(y)

#
5*0.6 - 0.5*9.81*0.6**2


# Problema 2.2
a = 5.0; b = 5.0; c = 5.0
a/b + c + a*c 
a/(b + c) + a*c 
a/(b + c + a)*c 

# Problema 2.3
import math 
p = 1; c = -1.5
a1 = math.sqrt(4*p + c)
print(a1)

#
import numpy
a2 = numpy.sqrt(4*p + c)
print(a2)
print(a2-a1)

# Problema 2.4
import math 
import numpy
x=1 
print(' sin({0:g})={1:g}'.format(x,  math.sin(x)))
print(' sin({0:g})={1:g}'.format(x, numpy.sin(x)))
print(' sin({0:g})={1:10.3g}'.format(x,  math.sin(x)))
print(' sin({0:g})={1:10.3g}'.format(x, numpy.sin(x)))
print(' sin({0:f})={1:f}'.format(x,  math.sin(x)))
print(' sin({0:f})={1:f}'.format(x, numpy.sin(x)))
print(' sin({0:f})={1:10.3f}'.format(x,  math.sin(x)))
print(' sin({0:f})={1:10.3f}'.format(x, numpy.sin(x)))

# Problema 2.5
del x, y; 
# x=1 ; y = 2 
print(' x = {0:f} e y = {1:f}'.format(x,  y))
x=1 # y = 2
print(' x = {0:f} e y = {1:f}'.format(x,  y))
x=1 ; y = 2 # El # indica ignorar el resto de la linea
print(' x = {0:f} e y = {1:f}'.format(x,  y))

# Problema 2.6
del x, y; 
print(2.5e-10)
print(2.5*10**-10)
print(4.5e4)
print(4.5 * 10 ** 4)
print(4.5e4)
print(1e1)
print(e)
import numpy as np
print(np.e)
print(np.pi)
print(np.exp(1))

# Problema 2.7
import numpy as np
import matplotlib.pyplot as plt

mu, sigma = 10, 5
x = mu + sigma * np.random.randn(10000)

plt.hist(x, 50, normed=1, facecolor='g')
plt.xlabel('X')
plt.ylabel('Y')
plt.title(r'$\mu=10,\ \sigma=5$')
plt.grid(True)
plt.show()

# Problema 2.8
del x, y; 
x = 1
x + x + 1
from sympy import Symbol
x = Symbol('x')
x + x + 1
x.name
type(x)
s = x + x + 1
s**2
(s + 2)*(s - 3)
from sympy import expand, factor
expand( (s + 2)*(s - 3) )
factor( 4*x**2 + 2*x - 6 )
factor( x**3 + 3*x**2 + 3*x + 1 )

from sympy import pprint
pprint(s)
pprint(factor( x**3 + 3*x**2 + 3*x + 1 ))
pprint( expand( (s + 2)*(s - 3) ) )
from sympy import solve
solve( (s + 2)*(s - 3) ) 
solve( 4*x**2 + 2*x - 6 ) 
solve( s  ) 

