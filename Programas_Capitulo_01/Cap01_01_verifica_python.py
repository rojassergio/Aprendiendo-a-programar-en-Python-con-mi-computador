'''
@author: Sergio Rojas
@contact: rr.sergio@gmail.com
--------------------------
Contenido bajo
 Atribución-NoComercial-CompartirIgual 3.0 Venezuela (CC BY-NC-SA 3.0 VE)
 http://creativecommons.org/licenses/by-nc-sa/3.0/ve/

Creado en abril 18, 2016
'''

# Verificamos la version de Python instalada en el computador:
import sys
import platform
print("\n")
print("Detalles de Python: ")
print(sys.version)
print("\n")
print(str("Version de Python es: ")+str(platform.python_version()))

# Verificamos la version de Ipython instalada con Python: 
try:
  import IPython
  print(str("Version de IPython es: ")+str(IPython.__version__))
except ImportError:
  sys.exit("Error : IPython parece no estar instalado.")

# Verificamos la version de Numpy instalada con Python: 
try:
  import numpy
  print(str("Version de Numpy es: ")+str(numpy.__version__))
except ImportError:
  sys.exit("Error : Numpy parece no estar instalado.")

# Verificamos la version de Matplotlib instalada con Python: 
try:
  import matplotlib
  print(str("Version de Matplotlib es: ")+str(matplotlib.__version__))
except ImportError:
  sys.exit("Error : Matplotlib parece no estar instalado.")

# Testing SymPy
try:
  import sympy
  print(str("Version de Matplotlib es: ")+str(sympy.__version__))
except ImportError:
  sys.exit("Error : SymPy parece no estar instalado.")

# Verificamos la version de Scipy instalada con Python: 
try:
  import scipy
  print(str("Version de Scipy es: ")+str(scipy.__version__))
except ImportError:
  sys.exit("Error : Scipy parece no estar instalado.")

print("\n")
print("\t    Este computador parece estar listo para masticar numeros ....")
print("\n")
print("\n")

