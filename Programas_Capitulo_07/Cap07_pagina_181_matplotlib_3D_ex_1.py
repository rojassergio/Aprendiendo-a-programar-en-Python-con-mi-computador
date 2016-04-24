'''
@author: Sergio Rojas
@contact: rr.sergio@gmail.com
--------------------------
Contenido bajo
 Atribución-NoComercial-CompartirIgual 3.0 Venezuela (CC BY-NC-SA 3.0 VE)
 http://creativecommons.org/licenses/by-nc-sa/3.0/ve/

Creado en abril 23, 2016
'''

x = []
y = []
z = []

archivo = 'cap_07_matplotlib_3D_ex_1_glass.dat'

try:
    seAbreArchivo = open(archivo,'r')
    for linea in seAbreArchivo:
          data = linea.strip().split()
          x.append(float(data[0]))
          y.append(float(data[1]))
          z.append(float(data[2]))
    seAbreArchivo.close()
except Exception as errorCapturado:
    print("\t Ocurrio el error: *** {0:s} ***".format(type(errorCapturado)))

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import numpy as np

# OK
nfilas  = 16
ncolums = 16

X = np.array(x).reshape(nfilas,ncolums)
Y = np.array(y).reshape(nfilas,ncolums)
Z = np.array(z).reshape(nfilas,ncolums)

fig = plt.figure()
ax = fig.add_subplot(1,2,1, projection='3d')
ax.plot(x, y, z, 'ob-')

ax.set_xlabel('X',fontsize=16)
ax.set_ylabel('Y',fontsize=16)
ax.set_zlabel(r"$\phi$",fontsize=36)
ax.set_title(r"$Visualizaci\acute{o}n 3D$",fontsize=16)

ax = fig.add_subplot(1,2,2, projection='3d')
surf = ax.plot_surface(X, Y, Z,         
                       rstride=1,     
                       cstride=1,   
                       linewidth=1,
                       color='w'
                      )

ax.set_xlabel('X',fontsize=16)
ax.set_ylabel('Y',fontsize=16)
ax.set_zlabel(r"$\phi$",fontsize=36)
ax.set_title(r"$Visualizaci\acute{o}n 3D$",fontsize=16)

fig.tight_layout()
fig.savefig("fig_chap_07_3Dfig_ex_1.png")
plt.show()

