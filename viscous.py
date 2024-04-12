import numpy as np
import matplotlib.pyplot as plt

def viscous(b):
    r=0
    v=0
    t=0
    T=[]
    Y=[]
    V=[]
    while (t<10):
        T.append(t)
        Y.append(r)
        V.append(v)
        r=r+v*dt
    
        a=-b*v-9
        if abs(a)<0.00000001:
            a=0
        v=v+a*dt
        t+=dt
    return T, Y, V
dt=0.001


T,Y, V=viscous(0.45)

plt.plot(T,Y)

plt.show()



         
