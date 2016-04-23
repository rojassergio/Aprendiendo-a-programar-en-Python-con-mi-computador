'''
@author: Sergio Rojas
@contact: rr.sergio@gmail.com
--------------------------
Contenido bajo
 Atribución-NoComercial-CompartirIgual 3.0 Venezuela (CC BY-NC-SA 3.0 VE)
 http://creativecommons.org/licenses/by-nc-sa/3.0/ve/

Creado en abril 21, 2016
'''

def biseccion(f, a, b, tol=1.e-6):
    """
    Funcion que implenta el metodo de biseccion usando
    la instruccion for para encontrar raices reales de
    una funcion. 

      f: es la funcion a la cual se le determina alguna raiz
      a: valor menor del interval
      b: valor mayor del intervalo
    tol: es la tolerancia
 
    """
    fa = f(a)
    if fa*f(b) > 0:
        return None, None, None

    itera = [0]    # variable que acumula las iteraciones
    for i in itera:

        c = (a + b)*0.5
        fmed = f(c)

        if abs(b-a) < tol:
           return i, c, fmed

        if fa*fmed <= 0:
            b = c  # La raiz esta en el intervalo [a,c]
        else:
            a = c  # La raiz esta en el intervalo [c,b]
            fa = fmed

        itera.append(i + 1)  
        itera[i] = None
        #print(itera)

def f(x):
    """
    Define la funcion para la cual queremos encontrar alguna raiz
    """
    return (x**2 + 4.0*x - 4.0)   # usar (-6,-4)

tol = 1e-10
a, b = 0, 2   # raiz por buscar
a, b = -6, -4 # raiz en la grafica
iter, x, fx = biseccion(f, a, b, tol)
if x is None:
    print('\t f(x) NO cambia signo en el intervalo [{0:g},{1:g}]'.format(a, b))
else:
    print('\t En {0:d} iteraciones y con tolerancia de {1:g} la raiz es:'
                                                          .format(iter,tol)) 
    print('\t x = {0:g}, generando f({0:g}) = {1:g}'.format(x,fx))
