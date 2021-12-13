import numpy as np
import matplotlib.pyplot as plt
n=1000
x=[0]
y=[0]
lastx=x[0]
lasty=y[0]
h=1
l=1
for i in range(n):
  x.append (lastx+l)
  y.append (lasty)
  lastx+=l
  x.append (lastx)
  y.append (lasty+h)
  lasty+=h
plt.plot(x,y)
plt.show()
  