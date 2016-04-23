'''
@author: Sergio Rojas
@contact: rr.sergio@gmail.com
--------------------------
Contenido bajo
 Atribución-NoComercial-CompartirIgual 3.0 Venezuela (CC BY-NC-SA 3.0 VE)
 http://creativecommons.org/licenses/by-nc-sa/3.0/ve/

Creado en abril 21, 2016
'''

#In [1]: 
x = [12.3, 4.82, 2.3, 6.7]; y = [45.6, 23.12, 7.21, 1.2]

#In [2]: 
elementos = range(len(x))

#In [3]: 
print(elementos)

#In [4]: 
print(len(x) == len(y) == len(elementos))

#In [5]: 
milista = []

#In [6]: 
for i in elementos:
        milista.append([ x[i],y[i] ])
        print('x = {0:4.2f} ; y = {1:4.2f}'.format(x[i],y[i]))
        
#In [7]: 
print(milista)

#In [8]: 
print(zip(x,y))

#In [9]: 
milista = []

for i in zip(x,y):
       milista.append(i)
       print('x = {0:4.2f} ; y = {1:4.2f}'.format(i[0],i[1]))

#In [11]: 
print(milista)

#In [12]: 

