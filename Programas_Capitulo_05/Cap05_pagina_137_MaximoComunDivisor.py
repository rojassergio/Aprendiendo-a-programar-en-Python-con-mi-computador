'''
@author: Sergio Rojas
@contact: rr.sergio@gmail.com
--------------------------
Contenido bajo
 Atribución-NoComercial-CompartirIgual 3.0 Venezuela (CC BY-NC-SA 3.0 VE)
 http://creativecommons.org/licenses/by-nc-sa/3.0/ve/

Creado en abril 21, 2016
'''

def MaximoComunDivisor(a,b):
    """
   Funcion que implementa el Algoritmo de Euclides para
   calcular el maximo Comun Divisor entre dos numeros
   enteros, requeridos como argumentos de la funcion: a y b
    """
    if (type(a)==int and type(b)==int):   
        a = abs(a)
        b = abs(b)
        if a < b:
           c=a
           a=b
           b=c
    else:
         return None

    while b > 0:
        r = a % b # r recibe el resto de dividir a entre b. Siempre r < b
        a = b
        b = r

    return a

a = 198
b = 12600
mcd = MaximoComunDivisor(a,b)

if (mcd == 0 or mcd == None):
    print('\t Numeros dados son incorrectos: alguno es real o ambos son cero:')
    print('\t    a = {0} y b = {1}'.format(a, b))
else:
    print('\t {2} es el MCD entre a = {0} y b = {1}'.format(a, b, mcd))
