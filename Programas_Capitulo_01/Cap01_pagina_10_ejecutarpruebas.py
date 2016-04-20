'''
@author: Sergio Rojas
@contact: rr.sergio@gmail.com
--------------------------
Contenido bajo
 Atribución-NoComercial-CompartirIgual 3.0 Venezuela (CC BY-NC-SA 3.0 VE)
 http://creativecommons.org/licenses/by-nc-sa/3.0/ve/

Creado en abril 18, 2016
'''

print("\n")
print("\t  Se ejecutarán algunas pruebas para verfificar     ...")
print("\t       Ipython, NumPy, SciPy y Matplotlib           ...")
print("\t  CADA PRUEBA TOMA VARIOS MINUTOS (O INCLUSO HORAS) ...")
print("\t  SI DESEA FINALIZARLAS SIN QUE TERMINEN PRESIONE   ...")
print("\t     SIMULTANEAMENTE CTRL y la tecla C              ...")

# Con esta instruccion el codigo funciona en python 2 y 3
try: 
   input = raw_input
except NameError: 
   pass

print("\n")
print("\t  Desea ejecutar las pruebas basicas de IPYTHON:   ...")
ans = input("Para SI, ingrese S y luego presione RETURN: ")
if ans=='S':
  import IPython
  print("Ejecutando las pruebas de Ipython: ")
  IPython.test()

print("\n")
print("\t  Desea ejecutar las pruebas basicas de NUMPY:   ...")
ans = input("Para SI, ingrese S y luego presione RETURN: ")
if ans=='S':
   import numpy
   print("Ejecutando las pruebas de Numpy: ")
   numpy.test()

print("\n")
print("\t  Desea ejecutar las pruebas basicas de SCIPY:   ...")
ans = input("Para SI, ingrese S y luego presione RETURN: ")
if ans=='S':
  import scipy
  print("Ejecutando las pruebas de Scipy: ")
  scipy.test()

print("\n")
print("\t  Desea ejecutar las pruebas basicas de MATPLOTLIB:   ...")
ans = input("Para SI, ingrese S y luego presione RETURN: ")
if ans=='S':
  import matplotlib
  print("Ejecutando las pruebas de Matplotlib: ")
  matplotlib.test()

