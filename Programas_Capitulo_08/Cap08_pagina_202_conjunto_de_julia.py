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

def f(z):
  return z*z - 1

def iteraf(c):
  i =0
  x=f(c)
  #print('i = {0} ; x = {1}'.format(i,x))
  while i < 40:
    i = i + 1
    x=f(x)
    #print('i = {0} ; x = {1}'.format(i,x))
  return x

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
for i in range(200000):
   c = complex(random.uniform(-2., 2.), random.uniform(-2., 2))
   u=iteraf(c)
   if (abs(u)<2): 
      ax.plot(c.real, c.imag, 'r.', markersize=1)

ax.set_title('Conjunto de Julia del mapa $f(z) = z^2 + 1$', fontsize = 15)
ax.set_xlabel('Parte real', fontsize = 15)
ax.set_ylabel('Parte imaginaria', fontsize = 15)

ax.set_ylim([-2,2])
ax.set_xlim([-2,2])

fig.savefig("conjunto_julia_ex01.png")
tfin = time.time()
print('tiempo = {0} seg'.format(tfin - tini))
plt.show()
