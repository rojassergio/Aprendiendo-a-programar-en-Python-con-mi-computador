'''
@author: Sergio Rojas
@contact: rr.sergio@gmail.com
--------------------------
Contenido bajo
 Atribución-NoComercial-CompartirIgual 3.0 Venezuela (CC BY-NC-SA 3.0 VE)
 http://creativecommons.org/licenses/by-nc-sa/3.0/ve/

Creado en abril 23, 2016
'''

#In [1]: 
import matplotlib.pyplot as plt

#In [2]: 
x  = [1.5, 2.7, 3.8, 9.5,12.3]

#In [3]: 
y =  [3.8,-2.4, 0.35,6.2,1.5]

#In [4]: 
fig = plt.figure()

#In [5]: 
ax = fig.add_subplot(1, 1, 1)

#In [6]: 
ax.plot(x, y, 'ro', label='y Vs x')

#In [7]: 
ax.set_title('Etiqueta de la grafica', fontsize = 10)

#In [8]: 
ax.set_xlabel('Etiqueta del eje x', fontsize = 12)

#In [9]: 
ax.set_ylabel('Etiqueta del eje y', fontsize = 15)

#In [10]: 
ax.legend(loc='best')

#In [11]: 
fig.savefig("fig0.png")

#In [12]: 
plt.show()

#In [13]: 

