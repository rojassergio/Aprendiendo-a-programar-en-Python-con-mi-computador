#In [1]: 
import numpy as np

#In [2]: 
print(type(1j))

#In [3]: 
print(np.sqrt(-4+0j))

#In [4]: 
print(np.complex(-4,0))

#In [5]: 
print(np.sqrt(np.complex(-4,0)))

#In [6]: 
z1 = 2 + 3.5j

#In [7]: 
z2 = -2 - 3.5j

#In [8]: 
print(z1+z2)

#In [9]: 
print(z1*z2)

#In [10]: 
print(z1/z2)

#In [11]: 
print(z1.real)

#In [12]: 
print(z1.imag)

#In [13]: 
a = 3

#In [14]: 
b = 4

#In [15]: 
z = a + b*1j

#In [16]: 
print(z)

#In [17]: 
print(np.complex(a,b))

#In [18]: 
print(1j**4)

#In [19]: 
print(1j**3)

#In [20]: 
print(z1**3)

#In [21]: 
print(np.sqrt(z1))

#In [22]: 
print(np.angle(z1))

#In [23]: 
print(np.angle(z1, deg=True))

#In [24]: 
print(np.abs(z1))

#In [25]: 

