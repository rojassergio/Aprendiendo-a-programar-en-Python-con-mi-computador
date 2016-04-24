'''
@author: Sergio Rojas
@contact: rr.sergio@gmail.com
--------------------------
Contenido bajo
 Atribución-NoComercial-CompartirIgual 3.0 Venezuela (CC BY-NC-SA 3.0 VE)
 http://creativecommons.org/licenses/by-nc-sa/3.0/ve/

Creado en abril 23, 2016
'''

import matplotlib.pyplot as plt
import random
import numpy as np
import time

tini = time.time()
def f(z,c):
  return z*z + c

def iteraf(c):
  i =0
  x = 0j
  while i < 40:
    i = i + 1
    x=f(x,c)
    #print('i = {0} ; x = {1}'.format(i,x))
  return x


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
for i in range(300000):
   c = complex(random.uniform(-1.5, 1), random.uniform(-1., 1))
   z=iteraf(c)
   if (abs(z)<2): # or np.isnan(z)):
      ax.plot(c.real, c.imag, 'r.', markersize=.5)

ax.set_title('Conjunto de Mandelbrot de $f(z) = z^2 + c$', fontsize = 15)
ax.set_xlabel('Parte real', fontsize = 15)
ax.set_ylabel('Parte imaginaria', fontsize = 15)

tfin = time.time()
print('tiempo = {0} seg'.format(tfin - tini))

fig.savefig("my_mandelbrot.png")
plt.show()

