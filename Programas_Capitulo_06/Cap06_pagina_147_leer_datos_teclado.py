# -*- coding: utf-8 -*-

'''
@author: Sergio Rojas
@contact: rr.sergio@gmail.com
--------------------------
Contenido bajo
 Atribución-NoComercial-CompartirIgual 3.0 Venezuela (CC BY-NC-SA 3.0 VE)
 http://creativecommons.org/licenses/by-nc-sa/3.0/ve/

Creado en abril 23, 2016
'''


def myinput():
    """
    Esta función permite leer datos desde el
    teclado sin ocuparnos de estar usando
    python 2 o python 3
    """
    import sys
    if sys.version[0]=="2":
        a = raw_input('\t Escriba la respuesta y presione ENTER/RETURN:--> : ')
    elif sys.version[0]=="3":
        a = input('\t Escriba la respuesta y presione ENTER/RETURN:--> : ')
    return a

print('\n Ingresa tu nombre: ')
nombre = myinput()
print('\n Ingresa tu edad, {0:s}:'.format(nombre))
edad = int(myinput())
print('\n Ingresa tu estatura en metros, {0:s}:'.format(nombre))
altura = int(myinput())
print('\n Ingresa tu peso en kilogramos, {0:s}:'.format(nombre))
peso = int(myinput())

str1 = '\n {0:s} de {1:d} años, tiene la'.format(nombre, edad)
str2 = 'estatura de {0:d} m y pesa {1:d} kgs.\n'.format(altura, peso)
print(' *** {0:s} {1:s} *** '.format(str1, str2))

