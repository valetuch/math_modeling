import matplotlib.pyplot as plt
import numpy as np

def patabola_protter (a=1,b=1,c=0,k=1):
  x= np.arange(-10,10,0.01)

  y=a*x**2+b*x+c
  z=k/x

  plt.plot(x,y)
  plt.show()
  
patabola_protter()
