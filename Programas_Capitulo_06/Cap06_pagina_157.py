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
archivo = 'cap_06_datos_01_espacios.txt'
try:
    seAbreArchivo = open(archivo,'r')
    for linea in seAbreArchivo:
        print(linea.strip().split())
    seAbreArchivo.close()
except IOError:
    print("No se pudo abrir el archivo:  {0:s}".format(archivo))

#In [2]: 

