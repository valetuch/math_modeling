import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
 
frames = 100
t = np.linspace(0, 5, frames)
 
def move_func(z, t):
    y, v_y = z
    dydt = v_y
    dv_ydt = (-k*y-5*np.cos(t*w))/m
    return dydt, dv_ydt

v = 0.5
w=28
m=0.5
k=12.5
l=0.08


y0 = 0
v_y0 = v 
z0 =  y0, v_y0

sol = odeint(move_func, z0, t)
def solve_func(i, key):
    if key == 'point':
        x = 0
        y = sol[i, 0]
        tg = t[i]
    else:
        y = sol[:i, 0]
        x = np.zeros((len(y), ))
        tg = t[:i]
    return tg, y

fig, ax = plt.subplots()

ball, = plt.plot([], [], 'o', color='r')
ball_line, = plt.plot([], [], '-', color='r')

def animate(i):
  ball.set_data (solve_func(i,'point'))
  ball_line.set_data (solve_func(i,'line'))
ani = FuncAnimation(fig,
                        animate,
                        frames=frames,
                        interval=30)
edge=0.5
ax.set_ylim(-edge,edge)
ax.set_xlim(-edge,edge*20)
 
ani.save('my_anim.gif')