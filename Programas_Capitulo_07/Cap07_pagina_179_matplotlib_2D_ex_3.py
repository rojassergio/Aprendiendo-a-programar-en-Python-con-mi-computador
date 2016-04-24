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

x  = [1.5, 2.7, 3.8, 9.5,12.3]
y =  [3.8,-2.4, 0.35,6.2,1.5]

fig = plt.figure()
#---
ax1 = fig.add_subplot(1, 2, 1)
ax1.set_title('Etiqueta de la grafica 1', fontsize = 10)
ax1.set_xlabel('Etiqueta del eje x1', fontsize = 12)
ax1.set_ylabel('Etiqueta del eje y1', fontsize = 15)
ax1.plot(x, y, 'ro', label='y Vs x')
ax1.legend(loc='best')
#---
ax2 = fig.add_subplot(1, 2, 2)
ax2.plot(y, x, 'bx-', label='x Vs y', markersize=20, linewidth=2)
ax2.set_title('Etiqueta de la grafica 2', fontsize = 10)
ax2.set_xlabel('Etiqueta del eje x2', fontsize = 12)
ax2.set_ylabel('Etiqueta del eje y2', fontsize = 15)
ax2.legend(loc=0)

fig.tight_layout()
fig.savefig("fig2.png")
plt.show()
