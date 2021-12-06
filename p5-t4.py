import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
from math import pi
import math
n=1000  
phi0=0.01
phi1=8*pi
phi=np.linspace(phi0,phi1,n)
def log(b=0.02):
 r=np.exp(b*phi)
 x=[]
 y=[]
 for i in range(n):
   x.append(r[i]*np.cos(phi[i]))
   y.append(r[i]*np.sin(phi[i]))
 plt.plot(x,y)
 plt.show()
 
def arx(b=0.01):
 r=b*phi
 x=[]
 y=[]
 for i in range(n):
   x.append(r[i]*np.cos(phi[i]))
   y.append(r[i]*np.sin(phi[i]))
 plt.plot(x,y)
 plt.show()
def jezl(b=0.01):
 r=b/np.sqrt(phi)
 x=[]
 y=[]
 for i in range(n):
   x.append(r[i]*np.cos(phi[i]))
   y.append(r[i]*np.sin(phi[i]))
 plt.axis('equal')
 plt.plot(x,y)
 plt.show()
def poza(b=3):
 r=np.sin(b*phi)
 x=[]
 y=[]
 for i in range(n):
   x.append(r[i]*np.cos(phi[i]))
   y.append(r[i]*np.sin(phi[i]))
 plt.axis('equal')
 plt.plot(x,y)
 plt.show()

poza()
  