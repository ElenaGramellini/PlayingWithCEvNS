###############################
###      Important notes    ###
### the v is in mm/microsec ###
### the E is in V/cm       ###
###############################

import argparse
import math

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
# sps source
phi = 10e7

def V2P(V, T,m):
    p = pa2Atm*m*R*T/(V*M)
    return p


def mol2Nevent(nmol, phi):
    Nevt = nmol*Na*phi*sigma*secondsInAYear*numberOfYears
    return Nevt


def allparameters2Nevent(phi, p, V, T):
    nmol = p*V/(pa2Atm*R*T)
    Nevt = nmol*Na*phi*sigma*secondsInAYear*numberOfYears
    return Nevt


def rho2Nevt(rho, V):
    constFactor = phi*sigma*secondsInAYear*numberOfYears*Na/M
    Nevt = rho*V*constFactor
    return Nevt

def rho2P(rho, T):
    P = pa2Atm*rho*T*R/M
    return P


import matplotlib.pyplot as plt
import numpy as np


fig1 = plt.figure(facecolor='white')
t1 = np.arange(1., 30000., 0.5)
print t1
f2 = np.vectorize(rho2Nevt)
print f2( t1 , 1.  )
f3 = np.vectorize(rho2P)
#line1 = plt.plot(t1,f2( t1 , 0.5 ),label="$\phi = 10^7 cm^{-2} s^{-1}$, $\sigma = 10^{-40} cm^2 V=0.5$ $m^2$",linewidth=2.0)
#line2 = plt.plot(t1,f2( t1 , 1.  ),label="$\phi = 10^7 cm^{-2} s^{-1}$, $\sigma = 10^{-40} cm^2 V=1.0$ $m^2$",linewidth=2.0)
#line3 = plt.plot(t1,f2( t1 , 5.  ),label="$\phi = 10^7 cm^{-2} s^{-1}$, $\sigma = 10^{-40} cm^2 V=5.0$ $m^2$",linewidth=2.0)



line4 = plt.plot(t1,f3(t1, 300. ),label="T = 300 K",linewidth=2.0)
line5 = plt.plot(t1,f3(t1, 200. ),label="T = 200 K",linewidth=2.0)
line6 = plt.plot(t1,f3(t1, 100. ),label="T = 100 K",linewidth=2.0)

plt.legend(bbox_to_anchor=(0.9, 0.8),
           bbox_transform=plt.gcf().transFigure)

plt.grid(True)
plt.title('Estimated Number of Events for 1 year')
font = {'family': 'serif',
        'color':  'black',
        'weight': 'normal',
        'size': 30,
        }


#plt.semilogy()
plt.text(500, 0.5e4, r'$N_{Evt} = \phi\sigma N_{centers}$', fontdict=font)
plt.text(500, 0.5e3, r'$N_{centers} = N_{A}n_{mol}$', fontdict=font)
plt.xlabel(r'$\rho [kg m^{-3}]$', fontdict=font)
#plt.ylabel(r'$N_{Evt}$', fontdict=font)
plt.ylabel(r'P [atm]', fontdict=font)
plt.show()


#plt.plot(t1, E2v(t1,87), 'bo')

