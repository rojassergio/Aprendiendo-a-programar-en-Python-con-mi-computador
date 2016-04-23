'''
@author: Sergio Rojas
@contact: rr.sergio@gmail.com
--------------------------
Contenido bajo
 Atribución-NoComercial-CompartirIgual 3.0 Venezuela (CC BY-NC-SA 3.0 VE)
 http://creativecommons.org/licenses/by-nc-sa/3.0/ve/

Creado en abril 23, 2016
'''

# In [13]: %cpaste
def fdivide(x,y):
    try:
        print('{0}/{1} = {2}'.format(x, y, x/y))
    except ZeroDivisionError:
        print("\t En fdivide({0},{1})".format(x,y))
        print("\t Ocurrio el error: *** ZeroDivisionError ***")
    except TypeError:
        print("\t En fdivide({0},{1})".format(x,y))
        print("\t Ocurrio el error: *** TypeError ***")
    except Exception as errorCapturado:
        print("\t En fdivide({0},{1})".format(x,y))
        print("\t Ocurrio el error: *** {0:s} ***".format(type(errorCapturado)))

#In [14]: 
print(fdivide(2,3))

#In [15]: 
print(fdivide(2,3.))

#In [16]: 
print(fdivide(2,0))

#In [17]: 
print(fdivide(2, 'a'))

#In [18]: 
print(fdivide('a',0))

#In [19]: 
  
