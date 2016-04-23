'''
@author: Sergio Rojas
@contact: rr.sergio@gmail.com
--------------------------
Contenido bajo
 Atribución-NoComercial-CompartirIgual 3.0 Venezuela (CC BY-NC-SA 3.0 VE)
 http://creativecommons.org/licenses/by-nc-sa/3.0/ve/

Creado en abril 21, 2016
'''

def f(x):
    if (type(x)==int or type(x)==float or type(x)==complex):
        res = x*x
    else:
        res = x
    return res

a = [1, 2.4, 1 + 1j, 'abgdfr', 4]

print(f(a[0]))

print(f(a[1]))

print(f(a[2]))

print(f(a[3]))

print(f(a[4]))

b = map(f, a)

print(b)

print(type(a))
print(type(b))

try:
   print(map(f,203))
except TypeError:
   print("TypeError: argument 2 to map() must support iteration")
   print("Ejecutar el siguiente comando en la consola Ipython")
   print("\t map(f,203)")

print(map(f,'ab34gh'))

print(len(a))

print(a[-1])

print(a[len(a)-1])
