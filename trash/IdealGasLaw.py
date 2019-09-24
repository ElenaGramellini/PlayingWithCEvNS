###############################
###      Important notes    ###
### the v is in mm/microsec ###
### the E is in V/cm       ###
###############################

import argparse
import math

R = 8.314 # m3 Pa K-1
#m = 1000   # gr 
M = 20.1797 # gr/mol
pa2Atm = 9.86923e-6

def V2P(V, T,m):
    p = pa2Atm*m*R*T/(V*M)
    return p




import matplotlib.pyplot as plt
import numpy as np

fig1 = plt.figure(facecolor='white')
t1 = np.arange(0.1, 10.0, 0.1)
f2 = np.vectorize(V2P)
line1 = plt.plot(t1, f2(t1,100.,1000),label="T = 100 K, m = 1 Kg, 49.5 mols",linewidth=2.0)
line2 = plt.plot(t1, f2(t1,100.,10000),label="T = 100 K, m = 10 Kg, 495 mols",linewidth=2.0)
#line3 = plt.plot(t1, f2(t1,100.,100000),label="T = 100 K, m = 100 Kg, 4950 mols",linewidth=2.0)
#line2 = plt.plot(t1, f2(t1,200.,1),label="T = 200 K, m = 1 Kg, 49.5 mols",linewidth=2.0)
#line3 = plt.plot(t1, f2(t1,300.),label="T = 300 K, m = 1 Kg, 49.5 mols",linewidth=2.0)
#line4 = plt.plot(t1, f2(t1,93.0),label="T = 93.0 K",linewidth=2.0)
plt.legend(bbox_to_anchor=(0.8, 0.5),
           bbox_transform=plt.gcf().transFigure)

plt.grid(True)
plt.title('Ideal Gas Law Neon, molar Mass 20.2 g/mol')
font = {'family': 'serif',
        'color':  'black',
        'weight': 'normal',
        'size': 30,
        }
plt.text(1, 12, r'$PV = \frac{m}{M} RT$', fontdict=font)
plt.xlabel('Volume [m^3]')
plt.ylabel('Pressure [atm] ')
plt.show()


#plt.plot(t1, E2v(t1,87), 'bo')

