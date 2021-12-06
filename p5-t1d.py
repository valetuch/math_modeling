import numpy as np
import matplotlib.pyplot as plt
from math import sin
from math import pi
n=100
t0=0
t1=10
a=1
A=1
B=1
t=np.linspace(t0,t1,n)
l=pi/2

def lisajo(b=0.02):
 print("call l",b,n,A,B,a,l)
 x=[]
 y=[]
 for i in range(n):
   x.append(A*np.sin(a*t[i]+l))
   y.append(B*np.sin(b*t[i]))
 
 print(x,y)
 
 plt.plot(x,y)
 plt.show()

lisajo()