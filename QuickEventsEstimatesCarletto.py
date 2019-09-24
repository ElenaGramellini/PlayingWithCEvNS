import numpy as np
import matplotlib.pyplot as plt
from decimal import Decimal

import math

# Ideal gas constant
R     = 8.2057*1e-5 # m3 atm K-1 mol-1
# Good old avogadro  
Na    = 6.0221409e+23
# Coherent XS on Sodium
sigma = 1e-40 #cm^2
# Seconds in a year
secondsInAYear = 3.154e+7
# Number of years
numberOfYears = 1
# Neon molar mass
M = 20.1797e-3 # gr/mol 
# sps source cm-2 s-1
phi = 1e10

C = Na*phi*sigma*secondsInAYear/M

def rho2Nevt(rho, V):
    Nevt = C*rho*V
    return Nevt

def rho2P(rho, T):
    P = rho*T*R/M
    return P

def PV2Nevt(P, V, T):
    Nevt = C*V*P/T
    return Nevt


font = {'family': 'serif',
        'color':  'black',
        'weight': 'normal',
        'size': 20,
        }


t1       = np.arange(0.1, 2., 0.01)
evtEst   = np.vectorize(rho2Nevt)
pressure = np.vectorize(rho2P)


plt.figure(1,facecolor='white',figsize=(10,10))
plt.subplot(211)
line3 = plt.plot(t1,evtEst( t1 , 5.  ),label="$\phi = 10^{10} cm^{-2} s^{-1}$, $\sigma = 10^{-40} cm^2 V=5.0$ $m^3$",linewidth=2.0)
line2 = plt.plot(t1,evtEst( t1 , 1.  ),label="$\phi = 10^{10} cm^{-2} s^{-1}$, $\sigma = 10^{-40} cm^2 V=1.0$ $m^3$",linewidth=2.0)
line1 = plt.plot(t1,evtEst( t1 , 0.5 ),label="$\phi = 10^{10} cm^{-2} s^{-1}$, $\sigma = 10^{-40} cm^2 V=0.5$ $m^3$",linewidth=2.0)
plt.ylabel(r'N$_{evt}$ per year', fontdict=font)
#plt.xlabel(r'$\rho$ [kg m$^{-3}$]', fontdict=font)
plt.grid(True)
plt.legend(bbox_to_anchor=(0.6, 0.9),
           bbox_transform=plt.gcf().transFigure)


plt.subplot(212)
line35 = plt.plot(t1,pressure(t1, 300. ),"--",label="T = 300 K",linewidth=2.0)
line4 = plt.plot(t1,pressure(t1, 150. ),"--",label="T = 150 K",linewidth=2.0)
line5 = plt.plot(t1,pressure(t1, 100. ),"--",label="T = 100 K",linewidth=2.0)
line6 = plt.plot(t1,pressure(t1, 70. ),"--" ,label="T = 70 K",linewidth=2.0)
#plt.ylim(0, 1.)
plt.legend(bbox_to_anchor=(0.3, 0.35),
           bbox_transform=plt.gcf().transFigure)
plt.xlabel(r'$\rho$ [kg m$^{-3}$]', fontdict=font)
plt.ylabel(r'P [atm]', fontdict=font)
plt.grid(True)

'''
plt.figure(2,facecolor='white',figsize=(10,10))
p1       = np.arange(0.1, 10., 0.1)
v1       = np.arange(0.1,  5., 0.1)
evtEst2  = np.vectorize(PV2Nevt)
line6 = plt.plot(t1,f3(t1, 100. ),"--",label="T = 100 K, V = 1 m$^{3}$",linewidth=2.0)
plt.ylim(0, 10.)
plt.legend(bbox_to_anchor=(0.7, 0.25),
           bbox_transform=plt.gcf().transFigure)
plt.xlabel(r'$\rho$ [kg m$^{-3}$]', fontdict=font)
plt.ylabel(r'P [atm]', fontdict=font)
plt.grid(True)
'''
plt.show()
