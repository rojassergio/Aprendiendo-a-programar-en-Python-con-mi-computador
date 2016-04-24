'''
@author: Sergio Rojas
@contact: rr.sergio@gmail.com
--------------------------
Contenido bajo
 Atribución-NoComercial-CompartirIgual 3.0 Venezuela (CC BY-NC-SA 3.0 VE)
 http://creativecommons.org/licenses/by-nc-sa/3.0/ve/

Creado en abril 23, 2016
'''

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

x = [0.0, 1.5, 3.0, 4.5, 6.0, ]
y = [0.0, 0.86, 1.71, 2.57, 3.43, 4.29, 5.14, 6.0]

X, Y  = np.meshgrid(x,y)

Z = 4*X**2 + Y**2

fig = plt.figure()
ax = fig.add_subplot(1,2,1, projection='3d')
ax.plot(X.flatten(), Y.flatten(), Z.flatten(), 'ob')
ax.plot_wireframe(X, Y, Z, rstride=1, cstride=1, color='r')

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
fig.savefig("fig_chap_07_3Dfig_ex_2.png")
plt.show()

