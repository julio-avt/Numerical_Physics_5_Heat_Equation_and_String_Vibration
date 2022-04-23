# -*- coding: utf-8 -*-
"""
@author: Julio C. Torreblanca
"""

from numpy import *;import matplotlib.pylab as p
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

"""
    Nx = intervalo para la variable x [0,Nx]
    Nt = valores que consideraremos para t, pero más adelante 
         tomaremos saltos en t para hacer más preciso el cálculo.
    Dx = valor de delta x
    Dt = valor de delta t
    K  = conductividad térmica
    C  = capacidad calorífica
    rho= densidad del material
    T  = es una lista auxiliar que permitirá hacer cálculos para
         obtener las temperaturas a un tiempo posterior
    Tpl= es arreglo con las temperaturas para cada punto del espacio.
"""

Nx=100; Nt=20000; Dx=0.03;  Dt=5.
#Aluminio:
K = 205.; C = 910.; rho = 2700.
#Madera de pino:
#K = 0.12; C = 2510.; rho = 640.
T=zeros((Nx,2),float) #lista auxiliar para j, j+1
Tpl=zeros((Nx,100),float) #lista con todos los calculos

print(" Trabajando")
for ix in range(1,Nx-1):
    T[ix,0]=100.0;     # T condicion inicial



T[0,0]=0.0; T[0,1]=0.  # Primero y ultimo T = 0
T[Nx-1,0]=0.0;T[Nx-1,1]=0.0

cons=K/(C*rho)*Dt/(Dx*Dx);

print(cons)
m=1      # Contador
for t in range(1,Nt):
    for ix in range(1,Nx-1):
        T[ix,1] = T[ix,0]+cons*(T[ix+1,0]+T[ix-1,0]-2.0*T[ix,0])
    if t%300==0 or t==1:
        for ix in range(1,Nx-1,2): Tpl[ix,m]=T[ix,1]
        print(m)
        m=m+1
    for ix in range(1,Nx-1): T[ix,0]=T[ix,1]
    

x=list(range(1,Nx,2))
y=list(range(1,30)) #Modificar para el tiempo
X,Y=p.meshgrid(x,y)


def functz(Tpl):
    z=Tpl[X,Y]
    return z

Z=functz(Tpl)
fig=p.figure()   # Crea la figura
ax=Axes3D(fig)
#ax.plot_wireframe(X,Y,Z,color='b')
ax.plot_surface(X, Y, Z, cmap=cm.coolwarm)
ax.set_xlabel('Posicion $x$')
ax.set_ylabel('tiempo $t$')
ax.set_zlabel('Temperatura $T$')
p.show()
print("Game over")