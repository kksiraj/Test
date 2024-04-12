import numpy as np
import matplotlib.pyplot as plt
r=np.array([0,0,0])
v=np.array([1,0,0])
b=np.array([0,-1,0])
dt=0.001
t=0
x=[]
y=[]
z=[]
#q/m=1
while (t<10):
    x.append(r[0])
    y.append(r[1])
    z.append(r[2])
    a=np.cross(v,b)
    r=r+v*dt
    v=v+a*dt
    t+=dt
k=plt.axes(projection="3d")
k.plot3D(x,y,z)
plt.show()
    
