import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
 
fig, ax = plt.subplots()
line, = plt.plot([], [], '--', color='red', label='line')
 
edge = 10
 
plt.axis('equal')
 
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
 
x, y = [], []
 
def animate(frame):
    t = frame
    dd = np.exp(np.cos(t)) - 2*np.cos(4*t) + (np.sin(t/12))**5
    xn = np.sin(t)*dd
    yn = np.cos(t)*dd
 
    x.append(xn)
    y.append(yn)
    line.set_data(x, y)
 
ani = animation.FuncAnimation(fig,
                        animate,
                        frames=np.arange(0, 10, 0.1),
                        interval=30)
 
ani.save('my_anim.gif')