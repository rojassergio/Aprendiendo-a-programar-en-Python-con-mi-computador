'''
@author: Sergio Rojas
@contact: rr.sergio@gmail.com
--------------------------
Contenido bajo
 Atribución-NoComercial-CompartirIgual 3.0 Venezuela (CC BY-NC-SA 3.0 VE)
 http://creativecommons.org/licenses/by-nc-sa/3.0/ve/

Creado en abril 21, 2016
'''

import keyword
print(keyword.kwlist)

try:
    exec('a = 8.0')
    print("\t Dentro de la instruccion TRY a = {0}".format(a))
    exec('else = 8.0')
except SyntaxError:
    print("Oops!  Dentro de la instruccion TRY ")
    print("       Has intentado asignarle a 'else' un valor.")
    print("       Como 'else' es un nombre reservado, no se")
    print("       le puede asignar un valor y se produce ")
    print("       un 'SyntaxError' que hace se muestre en pantalla ")
    print("       esta nota.")

