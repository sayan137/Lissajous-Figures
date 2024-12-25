import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation 
from matplotlib.animation import PillowWriter


#8~13 are customizable
a=3 #amplitude
b_1=2
phase=1*np.pi #phase difference
omega_a=2 #angular frequency
omega_b=3
fs=30 #frame speed
theta=1/2*np.pi

t=np.linspace(0,16*np.pi,20000)
u=b_1*np.cos(theta)
b=b_1*np.sin(theta)
ph=phase+np.pi/2
x=a*np.cos(omega_a*t)+u*np.cos(omega_b*t+ph)
y=a*np.sin(omega_a*t)+u*np.cos(omega_b*t+ph)
xv=b*np.cos(omega_b*t+ph)
yv=b*np.sin(omega_b*t+ph)

g=(ph-np.pi/2)/np.pi
thet=theta/np.pi

fig, ax=plt.subplots(2,2,figsize=(8,8))

p=ax[1][1]
p.arrow(0, 0, a, 0,
          length_includes_head=True,
          width=0.01,
          edgecolor='black',
          facecolor='green',
          lw=2,
          zorder=2)
p.set_xlim(-4,4)
p.set_ylim(-4,4)

q=ax[0][0]
q.arrow(0, 0, 0, b,
          length_includes_head=True,
          width=0.01,
          edgecolor='black',
          facecolor='green',
          lw=2,
          zorder=2)
q.set_xlim(-4,4)
q.set_ylim(-4,4)

r=ax[0][1]
r.set_xlim(-4,4)
r.set_ylim(-4,4)

s=ax[1][0]
s.set_xlim(-4,4)
s.set_ylim(-4,4)

hh=[max(y),max(x),max(xv),max(yv)]
h=round(max(hh))
h=h+1


def animate(i):
    p.cla() 
    circle = plt.Circle((0, 0), max(y), edgecolor='#666600', fill=False)
    p.add_patch(circle) 
    p.arrow(0, 0, x[fs*i], y[fs*i],
          length_includes_head=True,
          width=0.01,
          edgecolor='black',
          facecolor='green',
          lw=2,
          zorder=2)
    p.arrow(0, 0, 0, y[fs*i],
          length_includes_head=True,
          width=0.01,
          edgecolor='red',
          facecolor='green',
          lw=2,
          zorder=2)
    p.arrow(0, 0, x[fs*i], 0,
          length_includes_head=True,
          width=0.01,
          edgecolor='#3300FF',
          facecolor='green',
          lw=2,
          zorder=2)
    
    p.axvline(x=x[fs*i],alpha=0.3,color='red')
    p.set_xlim(-h,h)
    p.set_ylim(-h,h)
    p.set_aspect('equal')
    p.grid(True,alpha=0.3)
    p.axhline(y=0,color="black",linewidth=1,alpha=0.5)
    p.axvline(x=0,color="black",linewidth=1,alpha=0.5)

    q.cla()
    circle = plt.Circle((0, 0), b, edgecolor='#666600', fill=False)
    q.add_patch(circle) 
    q.arrow(0, 0, xv[fs*i], yv[fs*i],
          length_includes_head=True,
          width=0.01,
          edgecolor='black',
          facecolor='green',
          lw=2,
          zorder=2)
    q.arrow(0, 0, 0, yv[fs*i],
          length_includes_head=True,
          width=0.01,
          edgecolor='red',
          facecolor='green',
          lw=2,
          zorder=2)
    q.arrow(0, 0, xv[fs*i], 0,
          length_includes_head=True,
          width=0.01,
          edgecolor='#3300FF',
          facecolor='green',
          lw=2,
          zorder=2)
    
    q.axhline(y= yv[fs*i],alpha=0.3,color='red')
    q.set_xlim(-h,h)
    q.set_ylim(-h,h)
    q.set_aspect('equal')
    q.grid(True,alpha=0.3)
    q.axhline(y=0,color="black",linewidth=1,alpha=0.5)
    q.axvline(x=0,color="black",linewidth=1,alpha=0.5)

    r.cla()
    r.plot(x[:fs*i],yv[:fs*i],color='#7B1FA2') 
    r.axhline(y= yv[fs*i],alpha=0.3,color='red')
    r.axvline(x=x[fs*i],alpha=0.3,color='red')
    r.set_xlim(-h,h)
    r.set_ylim(-h,h)
    r.set_aspect('equal')
    r.grid(True,alpha=0.3)

    s.text(-3.5,1,f'x={a}cos({omega_a}t)',fontsize=20,color='black')
    s.text(-3.5,-1,f'y={b_1}cos({omega_b}t+{round(g,2)}$\\pi$)',fontsize=20,color='black')
    s.text(-3,-2,f'angle between x & y={round(thet,2)}$\\pi$',fontsize=10,color='black')
    s.set_aspect('equal')


ani=animation.FuncAnimation(fig,animate,frames=300,interval=50)
ani.save('Lovelace/ani.gif',writer='pillow',fps=30,dpi=100)
#plt.show()

