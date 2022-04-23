# -*- coding: utf-8 -*-
"""
@author: Julio C. Torreblanca
"""
from math import pi, sin, exp
import numpy as np
import matplotlib.pylab as p
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm


def T(x, t):
    """Esta funcion evalua los primeros 1000 terminos de la serie en la 
    solución analítica para el aluminio"""
    n = 1000
    K = 205.0 
    C = 910.0
    rho = 2700.0
    suma = 0
    
    c = K/(rho * C)
    
    if x == 1. or x == 0.:
        return 0
    elif t == 1:
        return 100
    else:
        for i in range(1, n,2):
            suma += 400/(i*pi) * sin(i * pi *x) * exp(-(i*pi)**2 * t*c)
            
    return suma

Tpl = np.zeros((100, 100), float)   

m = 1
prueba = np.zeros((100), float)
x = np.linspace(0, 1, 100)

for t in range(1, 20000):
    if (t%300 == 0) or (t==1):
        for ix in range(1, 100):
            Tpl[ix, m] = T(x[ix], t)
        print(m)
        m += 1
    
x = list(range(1, 100))
y = list(range(1, 30))

X, Y = p.meshgrid(x, y)

def functz(Tpl):
    z = Tpl[X, Y]
    return z

Z = functz(Tpl)
fig = p.figure()
ax = Axes3D(fig)
#ax.plot_wireframe(X, Y, Z, color="b")
ax.plot_surface(X, Y, Z, cmap=cm.coolwarm) 
ax.set_xlabel('Posición $(x)$') 
ax.set_ylabel('tiempo $(t)$')
ax.set_zlabel('Temperatura ($T$)')
p.show()
