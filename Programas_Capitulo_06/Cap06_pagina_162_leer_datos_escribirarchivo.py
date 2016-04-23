'''
@author: Sergio Rojas
@contact: rr.sergio@gmail.com
--------------------------
Contenido bajo
 Atribución-NoComercial-CompartirIgual 3.0 Venezuela (CC BY-NC-SA 3.0 VE)
 http://creativecommons.org/licenses/by-nc-sa/3.0/ve/

Creado en abril 23, 2016
'''

import sys
a= dict() # one can also use  a= {}

a['Iris-setosa']=[[], [], [], []]
a['Iris-versicolor']=[[], [], [], []]
a['Iris-virginica']=[[], [], [], []]

archivo = 'iris.data'
try:
    with open(archivo, 'r') as seAbreArchivo:
      for linea in seAbreArchivo:
        data = linea.strip().split(',')
        nombre = data.pop(-1) #extrae y asigna a nombre ultimo elemento en data 
        i=0
        while i < len(data):
          a[nombre][i].append(float(data[i]))
          i += 1 # recordar que es equivalente a: i = i + 1
except Exception as errorCapturado:
    print("\t Abriendo archivo para lectura ")
    print("\t Ocurrio el error: *** {0:s} ***".format(type(errorCapturado)))
    sys.exit(1)

import scipy.stats
archivoEscribir = 'iris_stadistica.data'
str0=': Nro datos : minimo-maximo : Promedio : Variancia : Skewness : Kurtosis'
label=['Sepalo L', 'Sepalo A', 'petalo L', 'petalo A']
try:
    with open(archivoEscribir, 'w') as seAbreArchivoE:
	for flortipo in a.keys():
	  totalcols = len(a[flortipo])
	  seAbreArchivoE.write('{0:^15} {1}\n'.format(flortipo,str0))
	  for columns in range(totalcols):
	     temp = scipy.stats.describe(a[flortipo][columns])
	     str1 = '{0: >12} {1: >10} {2:>11.3f}---{3:5.3f} {4:>8.3f}'.format(
		      label[columns],temp[0],temp[1][0],temp[1][1],temp[2])
	     str2 = '{0:>11.3f} {1:>10.3f} {2:>10.3f}'.format(
                                                 temp[3],temp[4],temp[5])
	     seAbreArchivoE.write('{0} {1}\n'.format(str1, str2))
except Exception as errorCapturado:
    print("\t Abriendo archivo para escritura")
    print("\t Ocurrio el error: *** {0:s} ***".format(type(errorCapturado)))
    sys.exit(1)
