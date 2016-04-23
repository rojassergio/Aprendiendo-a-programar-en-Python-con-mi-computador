'''
@author: Sergio Rojas
@contact: rr.sergio@gmail.com
--------------------------
Contenido bajo
 Atribución-NoComercial-CompartirIgual 3.0 Venezuela (CC BY-NC-SA 3.0 VE)
 http://creativecommons.org/licenses/by-nc-sa/3.0/ve/

Creado en abril 23, 2016
'''

# In [7]: %cpaste
def fdivide(x,y):
    try:
        print('{0}/{1} = {2}'.format(x, y, x/y))
    except Exception as errorCapturado:
        print("\t En fdivide({0},{1})".format(x,y))
        print("\t Ocurrio el error: *** {0:s} ***".format(type(errorCapturado)))

#In [8]: 
print(fdivide(2,3))

#In [9]: 
print(fdivide(2,3.))

#In [10]: 
print(fdivide(2,0))

#In [11]: 
print(fdivide(2, 'a'))

#In [12]: 
print(fdivide('a',0))

