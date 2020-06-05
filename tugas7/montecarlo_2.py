from scipy import random
import numpy as np

a = -1
b = 1
N=100
xrand=np.zeros(N)
yrand=np.zeros(N)
zrand=np.zeros(N)
integral=0.0
for i in range(4):
    for i in range(len(xrand)):
        xrand[i]=random.uniform(a,b)

    for i in range(len(yrand)):
        yrand[i]=random.uniform(a,b)

    for i in range(len(zrand)):
        zrand[i]=random.uniform(a,b)

    def func(x,y,z):
        return (x**2)+(y**2)+(z**2)


    for i in range(N):
        integral+=func(xrand[i],yrand[i],zrand[i])

jawab=(b-a)/float(N)*integral
print("jawab: ",jawab)
