'''
@author: Sergio Rojas
@contact: rr.sergio@gmail.com
--------------------------
Contenido bajo
 Atribución-NoComercial-CompartirIgual 3.0 Venezuela (CC BY-NC-SA 3.0 VE)
 http://creativecommons.org/licenses/by-nc-sa/3.0/ve/

Creado en abril 18, 2016
'''

import numpy as np
import matplotlib.pyplot as plt

#Figura en blando y negro
x = np.random.randn (10000) ; plt.hist (x, bins =40 , color ='w') ;
plt.show()

#Figura en verde
plt.hist (x, bins =40 , color ='g') ;
plt.show()
