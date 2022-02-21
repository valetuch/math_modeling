import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

x=np.arange(-5, 5, 0.01)




def diff_func(v, x):
  y, z = v
  dydx= y**2 * z
  dzdx = z/x - y * z**2
  return dydx, dzdx



y0 = 1
z0 = -3


v0 = y0, z0


sol = odeint (diff_func, v0, x)

plt.plot(sol[:, 0], sol[:, 1], 'g')
plt.legend()
plt.show()