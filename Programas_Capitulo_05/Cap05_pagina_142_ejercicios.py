'''
@author: Sergio Rojas
@contact: rr.sergio@gmail.com
--------------------------
Contenido bajo
 Atribución-NoComercial-CompartirIgual 3.0 Venezuela (CC BY-NC-SA 3.0 VE)
 http://creativecommons.org/licenses/by-nc-sa/3.0/ve/

Creado en abril 21, 2016
'''

#Problema 5.2
#-------------
x = 'abc'
def f():
    return x
print(x)
print(f())

#Problema 5.3
#-------------
x = 23.0
a = 'abc'
def f(a):
    x = a * a
    return x
y = f(3)
print(x)
print(y)

#Problema 5.8
#-------------
milista = [ 'a', 'b', 'c' ]
for i in milista:
    print(i)
    for j in milista: 
        print(j) 

