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
mitupla = ((0.0, 1.0, 2.3, 4.5), ['abc'], 3, '234ed')

#In [2]: 
print(mitupla)

#In [3]: 
mitupla[1][0] = mitupla[1][0] + mitupla[1][0]

#In [4]: 
print(mitupla)

#In [5]: 
mitupla[1][0] = mitupla[1] + [1,2,3]

#In [6]: 
print(mitupla)

#In [7]: 


