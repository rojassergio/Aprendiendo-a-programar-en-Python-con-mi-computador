'''
@author: Sergio Rojas
@contact: rr.sergio@gmail.com
--------------------------
Contenido bajo
 Atribución-NoComercial-CompartirIgual 3.0 Venezuela (CC BY-NC-SA 3.0 VE)
 http://creativecommons.org/licenses/by-nc-sa/3.0/ve/

Creado en abril 23, 2016
'''

def myinput(par):
    """
    Esta funcion permite leer datos desde el
    teclado sin ocuparnos de estar usando
    python 2 o python 3
    """
    import sys
    prueba = True
    while prueba:
        if sys.version[0]=="2":
            a = raw_input('\t Escriba la respuesta y presione ENTER/RETURN:--> : ')
        elif sys.version[0]=="3":
            a = input('\t Escriba la respuesta y presione ENTER/RETURN:--> : ')

        if par == 'int':
           try:
               prueba = False
               a = int(a)
           except:
               prueba = True
               print("NO es correcta la entrada '" + str(a) + "'")
               print("Por favor ingrese un numero entero: ")
        elif par == 'float':
           try:
               prueba = False
               a = float(a)
           except:
               prueba = True
               print("NO es correcta la entrada '" + str(a) + "'")
               print("Por favor ingrese un numero real usando punto: ")
        else:
               prueba = False
    return a

print('\n Ingresa tu nombre: ')
nombre = myinput('str')
print('\n Ingresa tu edad, {0:s}:'.format(nombre))
edad = myinput('int')
print('\n Ingresa tu estatura en metros, {0:s}:'.format(nombre))
altura = myinput('float')
print('\n Ingresa tu peso en kilogramos, {0:s}:'.format(nombre))
peso = myinput('float')

str1 = '\n {0:s} de {1:d} a~nos, tiene la'.format(nombre, edad)
str2 = 'estatura de {0:3.2f} m y pesa {1:5.2f} kgs.\n'.format(altura, peso)
print(' *** {0:s} {1:s} *** '.format(str1, str2))

