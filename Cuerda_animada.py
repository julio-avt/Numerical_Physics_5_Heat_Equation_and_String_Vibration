# -*- coding: utf-8 -*-
"""
@author: Julio C. Torreblanca
"""

from os import linesep
from numpy import *
import numpy as np, matplotlib.pyplot as plt
import matplotlib.animation as animation

rho = 0.05 #Densidad en kg/m
ten = 10. #Tension en  Newtons
c = sqrt(ten/rho)
c1 = c
Dt = 0.1  
Dx = 10.
ratio = sqrt(ten/rho)* Dt/Dx
print(ratio)
xi = np.zeros((101, 3), float)
k = range(0, 101)

def Initialize():
    for i in range(0, 100):
        xi[i, 0] = 0.00125 * i
    for i in range(81, 101):
        xi[i, 0] = 0.1 - 0.005*(i-80)
        
def animate(num):
    for i in range(1, 100):
        xi[i, 2] = 2* xi[i, 1] - xi[i, 0] + ratio*(xi[i + 1, 1]
                                                + xi[i-1, 1] - 2*xi[i, 1])
    line.set_data(k, xi[k, 2])
    for m in range(0, 101):
        xi[m, 0] = xi[m, 1]
        xi[m, 1] = xi[m, 2]
    return line

Initialize()

fig = plt.figure()
ax = fig.add_subplot(111, autoscale_on=False, xlim=(0, 101),
                     ylim=(-0.15, 0.15))
ax.grid()
plt.title('Vibraciones')
line , = ax.plot(k, xi[k,0] , lw=2)
for i in range(1, 100):
    xi[i, 1] = xi[i, 0] + 0.5*ratio*(xi[i+1, 0] + xi[i-1, 0]
                                     - 2*xi[i, 0])
ani = animation.FuncAnimation(fig, animate, 1)
plt.show()