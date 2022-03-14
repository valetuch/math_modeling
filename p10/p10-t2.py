import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math

t=np.arange(-1, 1, 0.01)




def diff_func(v, t):
  y, x = v
  dydx= 3*x-2*y+(np.exp(3*t)/np.exp(t)+1)
  dzdx = x-(np.exp(3*t)/np.exp(t)+1)
  return dydx, dzdx



x0 = 5
y0 = -7

v0=x0,y0


sol = odeint (diff_func, v0, t)

plt.plot(t, sol[:, 1], 'g')
plt.plot(t,sol[:, 0], 'g')
plt.legend()
plt.show()