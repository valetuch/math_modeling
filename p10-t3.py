import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math

x=np.arange(-5, 5, 0.01)




def diff_func(v, t):
  y, x = v
  dydx= x
  dzdx = np.sin(x)+np.cos(x)
  return dydx, dzdx



dy0= 0
y0 = 3

v0=y0,dy0


sol = odeint (diff_func, v0, x)

plt.plot(sol[:,0], sol[:, 1], 'g')

plt.legend()
plt.show()