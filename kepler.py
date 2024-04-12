import numpy as np
import matplotlib.pyplot as plt

    

def kepler():
    r=np.array([1,0])
    v=np.array([0,1.2])
    t=0
    X=[]
    Y=[]
    T=[]
    dA=[]
    while (t<100):
        da=0.5*np.cross(r,v*dt)
        dA.append(da)
        X.append(r[0])
        Y.append(r[1])
        T.append(t)
        r=r+v*dt
        a=-r/(np.linalg.norm(r))**3
        da=0.5*np.cross(r,v*dt)
        v=v+a*dt
        t+=dt
    return X, Y, dA


dt=0.001


X,Y, DA=kepler()

A1=sum(DA[1:10])
A2=sum(DA[11:20])
print(round(A1,3),round(A2,3))


plt.show()



         
