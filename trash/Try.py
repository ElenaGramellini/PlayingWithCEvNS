import numpy as np
from numpy import exp,arange
from pylab import meshgrid,cm,imshow,contour,clabel,colorbar,axis,title,show



# Ideal gas constant
R     = 8.314 # m3 Pa K-1
# Good old avogadro  
Na    = 6.0221409e+23
# Coherent XS on Sodium
sigma = 1e-40 #cm^2
# Seconds in a year
secondsInAYear = 3.154e+7
# Number of years
numberOfYears = 1
# Neon molar mass
M = 20.1797 # gr/mol 
# Pascal to atm Conversion 
pa2Atm = 9.86923e-6
# sps source cm-2 s-1
phi = 2*1e7

C = Na*phi*sigma*secondsInAYear/M

def PV2Nevt(P, V, T):
    Nevt = C*V*P/(T*pa2Atm)
    return Nevt

p1       = np.arange(0.1, 10., 0.1)
v1       = np.arange(0.1,  5., 0.1) 
X,Y = meshgrid(p1, v1) # grid of point
Z = PV2Nevt(X, Y,100) # evaluation of the function on the grid

im = imshow(Z,cmap=cm.RdBu) # drawing the function
# adding the Contour lines with labels
cset = contour(Z,arange(-1,1.5,0.2),linewidths=2,cmap=cm.Set2)
clabel(cset,inline=True,fmt='%1.1f',fontsize=10)
colorbar(im) # adding the colobar on the right
# latex fashion title
title('N event per year as a function of P and V')
show()
