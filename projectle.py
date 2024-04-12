import numpy as np
import matplotlib.pyplot as plt

def projectile(b):
    r=np.array([0,0])
    v=np.array([v0*np.cos(th),v0*np.sin(th)])
    t=0
    X=[]
    Y=[]
    
    while (r[1]>=0):
        X.append(r[0])
        Y.append(r[1])
        r=r+v*dt
        a0=np.array([0,-g])
        a=a0-b*np.linalg.norm(v)*v
        v=v+a*dt
        t+=dt
    return X, Y

v0=float(input("Enter Projectile velocity "))
th=float(input("Enter Angle of Projectile in Degrees "))
th=np.pi/180*th
dt=0.001
g=9.8

X,Y=projectile(0)
XA,YA=projectile(0.2)
plt.plot(X,Y)
plt.plot(XA,YA)
plt.show()



         
