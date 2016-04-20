'''
@author: Sergio Rojas
@contact: rr.sergio@gmail.com
--------------------------
Contenido bajo
 Atribución-NoComercial-CompartirIgual 3.0 Venezuela (CC BY-NC-SA 3.0 VE)
 http://creativecommons.org/licenses/by-nc-sa/3.0/ve/

Creado en abril 19, 2016
'''

import matplotlib.pyplot as plt

x= [0.0 , 0.2 , 0.41 , 0.61 , 0.82 , 1.02 , 1.22 , 1.43 , 1.63 , 1.84 , \
    2.04 , 2.24 , 2.45 , 2.65]

y = [0.0 , 0.2 , 0.4 , 0.57 , 0.73 , 0.85 , 0.94 , 0.99 , 1.0 , \
     0.96 , 0.89 , 0.78 , 0.64 , 0.47]

plt.plot (x,y,'ro', linewidth =2)
plt.show()

plt.plot (x,y,'b--', linewidth =2)

plt.xlabel('X')
plt.ylabel('Y')
plt.title(r'$\mathbf{T\'{\i}tulo \, de \, la \, Gr\'afica }$')

plt.savefig('Mi_Figura.png')
plt.savefig('Mi_Figura.pdf')
plt.show()
