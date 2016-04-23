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
def f(x):
    if (type(x)==int or type(x)==float or type(x)==complex):
        res = x*x
    else:
        res = x
    return res

#In [2]: 
a = [1, 2.4, 1 + 1j, 'abgdfr', 4]

#In [3]: 
b = map(f, a)

#In [4]: 
print(b)

#In [5]: 
milista = []

#In [6]: 
for i in a:
        milista.append(f(i))

#In [7]: 
print(milista)

#In [8]: 
print(milista == b)

#In [9]: 
c = [f(i) for i in a]

#In [11]: 
print(c)

#In [13]: 
print(milista == c == b)

#In [14]: 

