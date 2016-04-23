'''
@author: Sergio Rojas
@contact: rr.sergio@gmail.com
--------------------------
Contenido bajo
 Atribución-NoComercial-CompartirIgual 3.0 Venezuela (CC BY-NC-SA 3.0 VE)
 http://creativecommons.org/licenses/by-nc-sa/3.0/ve/

Creado en abril 23, 2016
'''

# In [1]: %cpaste
def fdivide(x,y):
    try:
        print('{0}/{1} = {2}'.format(x, y, x/y))
    except:
        print("\t Un error ocurrio ...")

#In [2]: 
print(fdivide(2,3))

#In [3]: 
print(fdivide(2,3.))

#In [4]: 
print(fdivide(2,0))

#In [5]: 
print(fdivide(2, 'a'))

#In [6]: 
print(fdivide('a',0))

#In [7]: 

