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
midic = {'dias' : ['lu', 'ma', 'mi', 'ju', 'vi', 'sa', 'do'],\
               2    : (1,2,3,4),\
        'nombre' : 'Juan Parao'}

#In [2]: 
print(midic)

#In [3]: 
print(midic.keys())

#In [4]: 
print(midic.values())

#In [5]: 
print(midic.items())

#In [6]: 
otrodic = dict([('nombre', 'Juan Parao'),\
                    (2, (1, 2, 3, 4)),
                     ('dias', ['lu', 'ma', 'mi', 'ju', 'vi', 'sa', 'do'])])

#In [7]: 
print(otrodic)

#In [8]: 
print(midic[2])

#In [9]: 
print(midic['nombre'])

#In [10]: 
print(midic.get('nombre'))

#In [11]: 
midic['nombre'] = 'Juan Parao Segundo'

#In [12]: 
print(midic)

#In [13]: 
midic['Otro Dato'] = 'cantante'

#In [14]: 
print(midic)

#In [15]: 
print(midic.pop(2))

#In [16]: 
print(midic)

#In [17]: 
