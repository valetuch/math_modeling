import numpy as np
import matplotlib.pyplot as plt
  

plt.axes(projection = 'polar')
  

rads = np.arange(0, 2 * np.pi, 0.001) 
  

for rad in rads:
    r = rad
    plt.polar(rad, r, 'g.')
      
plt.show()