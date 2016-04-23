'''
@author: Sergio Rojas
@contact: rr.sergio@gmail.com
--------------------------
Contenido bajo
 Atribución-NoComercial-CompartirIgual 3.0 Venezuela (CC BY-NC-SA 3.0 VE)
 http://creativecommons.org/licenses/by-nc-sa/3.0/ve/

Creado en abril 23, 2016
'''

#In [1]: %cpaste
a= dict() # one can also use  a= {}
a['Iris.setosa']=[[], [], [], []]
a['Iris.versicolor']=[[], [], [], []]
a['Iris.virginica']=[[], [], [], []]

archivo = 'cap_06_datos_01_espacios.txt'
try:
    seAbreArchivo = open(archivo,'r')
    for linea in seAbreArchivo:
        data = linea.strip().split()
        nombre = data.pop(-1) #extrae y asigna a nombre ultimo elemento en data 
        i=0
        while i < len(data):
          a[nombre][i].append(float(data[i]))
          i += 1 # recordar que es equivalente a: i = i + 1
    seAbreArchivo.close()
except Exception as errorCapturado:
    print("\t Ocurrio el error: *** {0:s} ***".format(type(errorCapturado)))

#In [2]: 
print(a)

#In [3]: 
print(a.keys())

#In [4]: 
print(a[a.keys()[0]])

#In [5]: 
print(a[a.keys()[1]])

#In [6]: 
print(a[a.keys()[2]])

#In [7]: 
print(a[a.keys()[0]][0])

#In [8]: 
print(a[a.keys()[0]][2])

#In [9]: 

