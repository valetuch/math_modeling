import matplotlib.pyplot as plt
import numpy as np
import math
a=int(input())
b=int(input())
c=int(input())

def okr(R=10):
   x=np.arange(-a*R,b*R,c)
   y=np.arange(-a*R,b*R,c)
   x,y=np.meshgrid(x,y)
   fxy=x**2+y**2
   plt.contour (x,y,fxy, levels=[R**2])
   plt.show()
okr()


  
  

