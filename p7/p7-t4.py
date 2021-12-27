import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
 
fig, ax = plt.subplots()
dots, = plt.plot([], [], '--', color='red', label='dots')
dots2, = plt.plot([], [], 'o', color='blue', label='dots')
c=0.3
d=0.33
x0=0.1
y0=0.1
edge = 1
 
plt.axis('equal')
 
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
 

def fractal(xi,yi,d,c,n):
  x,y=[],[]
  x0,y0=xi,yi
  for _ in range (int(n)):
   xt=x0**2-y0**2+c
   yt=2*x0*y0+d
   x.append (xt)
   y.append (yt)
   x0,y0=xt,yt
  return x,y
def animate(i):
 dots.set_data (fractal(x0,y0,d,c,i))


ani = animation.FuncAnimation(fig,
                        animate,
                        frames=100,
                        interval=30)
 
ani.save('my_anim.gif')
  
