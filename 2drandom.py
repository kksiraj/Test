import numpy as np

import matplotlib.pyplot as plt
x=0
y=0
X=[]
Y=[]
N=1000
for i in range(N):
    X.append(x)
    Y.append(i)
    r=np.random.choice([0,1])
    if(r==1):
        x+=1
    else:
        x-=1
plt.plot(Y,X)
'''
plt.xlim([-10,10])
plt.ylim([-10,10])
'''
#plt.plot([0,x],[0,y], color="r")
#print(np.sqrt(x**2+y**2),np.sqrt(N))
plt.show()
