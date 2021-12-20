import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
 
fig, ax = plt.subplots()
line, = plt.plot([], [], '--', color='red', label='line')
edge = 40
 
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
 
x, y = [], []
t=np.arange(-10,10,0.01)
x = 12*np.cos(t)+ 8*np.cos(1.5*t)
y = 12*np.sin(t)-8*np.sin(1.5*t)
star, = plt.plot(x,y, '--', color='red', label='line')
t = np.pi /3
X = x*np.cos(t) - y*np.sin(t)
Y = y*np.cos(t) + x*np.sin(t)
star, = plt.plot(X,Y, '--', color='purple', label='line')

def rotate (x,y,angle):
    X= x*np.cos(angle) - y*np.sin(angle)
    Y= y*np.cos(angle) + x*np.sin(angle)
    return X,Y
def animate(a):
 line.set_data (rotate(x,y,a))
ani = animation.FuncAnimation(fig,
                        animate,
                        frames=np.arange(0, 10, 0.1),
                        interval=30)

ani.save('my_anim.gif')

