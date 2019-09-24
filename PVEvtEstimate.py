import matplotlib.pyplot as plt
#plt.style.use('seaborn-white')
import numpy as np

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
phi = 2*1e7


C = Na*phi*sigma*secondsInAYear/R

font = {'family': 'serif',
        'color':  'black',
        'weight': 'normal',
        'size': 20,
        }

def PV2Nevt(P, V, T):
    Nevt = C*V*P/T
    return Nevt


p1 = np.linspace(0.1, 2, 50)
v1 = np.linspace(0.1, 5, 40)

plt.figure(1,facecolor='white',figsize=(6,6))
plt.subplot(1, 2, 1)
plt.title('Estimated Number of Events for 1 year, 300 K')
X, Y = np.meshgrid(p1, v1)
Z = PV2Nevt(X, Y, 300)
plt.contourf(X, Y, Z, 20, cmap='YlGn')
plt.grid(True)
plt.xlabel(r'P [atm]', fontdict=font)
plt.ylabel(r'V [m$^{3}$]', fontdict=font)
#plt.zlabel(r'N$_{evt}$ per year', fontdict=font)
plt.colorbar();

plt.subplot(1, 2, 2)
plt.title('Estimated Number of Events for 1 year, 70 K')
X, Y = np.meshgrid(p1, v1)
Z = PV2Nevt(X, Y, 70)
plt.contourf(X, Y, Z, 20, cmap='RdBu')
plt.grid(True)
plt.xlabel(r'P [atm]', fontdict=font)
plt.ylabel(r'V [m$^{3}$]', fontdict=font)
#plt.zlabel(r'N$_{evt}$ per year', fontdict=font)
plt.colorbar();

plt.show()

