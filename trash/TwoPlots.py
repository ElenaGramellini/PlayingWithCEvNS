import numpy as np
import matplotlib.pyplot as plt
from decimal import Decimal

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
# sps source cm-2 s-1
phi = 1e7

C = Na*phi*sigma*secondsInAYear/M
print C, '%.2E' % Decimal(C), phi

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


font = {'family': 'serif',
        'color':  'black',
        'weight': 'normal',
        'size': 20,
        }


t1 = np.arange(1., 25000., 0.5)
f2 = np.vectorize(rho2Nevt)
f3 = np.vectorize(rho2P)


plt.figure(1,facecolor='white',figsize=(10,10))
plt.subplot(211)
line1 = plt.plot(t1,f2( t1 , 0.5 ),label="$\phi = 10^7 cm^{-2} s^{-1}$, $\sigma = 10^{-40} cm^2 V=0.5$ $m^2$",linewidth=2.0)
line2 = plt.plot(t1,f2( t1 , 1.  ),label="$\phi = 10^7 cm^{-2} s^{-1}$, $\sigma = 10^{-40} cm^2 V=1.0$ $m^2$",linewidth=2.0)
line3 = plt.plot(t1,f2( t1 , 5.  ),label="$\phi = 10^7 cm^{-2} s^{-1}$, $\sigma = 10^{-40} cm^2 V=5.0$ $m^2$",linewidth=2.0)
plt.ylabel(r'N$_{evt}$ per year', fontdict=font)
plt.grid(True)
plt.legend(bbox_to_anchor=(0.7, 0.9),
           bbox_transform=plt.gcf().transFigure)


plt.subplot(212)
line4 = plt.plot(t1,f3(t1, 300. ),"--",label="T = 300 K",linewidth=2.0)
line5 = plt.plot(t1,f3(t1, 200. ),"--",label="T = 200 K",linewidth=2.0)
line6 = plt.plot(t1,f3(t1, 100. ),"--",label="T = 100 K",linewidth=2.0)
plt.ylim(0, 10.)
plt.legend(bbox_to_anchor=(0.7, 0.25),
           bbox_transform=plt.gcf().transFigure)
plt.xlabel(r'$\rho$ [kg m$^{-3}$]', fontdict=font)
plt.ylabel(r'P [atm]', fontdict=font)
plt.grid(True)


plt.figure(2,facecolor='white',figsize=(10,10))
line6 = plt.plot(t1,f3(t1, 100. ),"--",label="T = 100 K, V = 1 m$^{3}$",linewidth=2.0)
plt.ylim(0, 10.)
plt.legend(bbox_to_anchor=(0.7, 0.25),
           bbox_transform=plt.gcf().transFigure)
plt.xlabel(r'$\rho$ [kg m$^{-3}$]', fontdict=font)
plt.ylabel(r'P [atm]', fontdict=font)
plt.grid(True)

plt.show()
