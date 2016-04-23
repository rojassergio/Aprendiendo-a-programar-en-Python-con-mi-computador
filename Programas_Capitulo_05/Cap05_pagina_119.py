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
a = [1, 2.4, 1 + 1j, 'abgdfr', 4]

#In [2]:
copiadeai = a

#In [3]: 
copiadeac = list(a)

#In [4]: 
copiadeai == copiadeac

#In [5]: 
a.remove(4)

#In [6]: 
print(copiadeai == copiadeac)

#In [7]: 
print(copiadeai == a)

#In [8]: 
print(copiadeai)

#In [9]: 
print(copiadeac)

#In [10]: 
print(a)

#In [11]: 
print(copiadeai.pop(2))

#In [12]: 
print(copiadeai == a)

#In [13]: 
