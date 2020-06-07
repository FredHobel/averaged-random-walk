import numpy as np
import matplotlib.pyplot as plt
import random as rn


j = 0
loop = 1000
innerloop = 1000

xmin = 20
ymin = 20

xmax = 25
ymax = 25

pathx = []
pathy = []

realpathx = np.zeros(loop*1000)
realpathy = np.zeros(loop*1000)

boundaryx = [xmin,xmax,xmax,xmin,xmin]
boundaryy = [ymin,ymin,ymax,ymax,ymin]

success = 0

for j in range(loop) :
    pathx = []
    pathy = []
    i = 0
    x = 0
    y = 0

    while i < innerloop :
        x += rn.uniform(-1,1)
        y += rn.uniform(-1,1)
        pathx.append(x)
        pathy.append(y)
        i += 1
        k = 0
        if x >= xmin and y >= ymin and x <= xmax and y <= ymax:
            i = innerloop + 1
            
            for k in range(len(pathx)):
                realpathx[k + success*1000] = pathx[k]
                realpathy[k + success*1000] = pathy[k]
                k += 1
            success += 1
    j += 1


averagex = np.zeros(innerloop)
averagey = np.zeros(innerloop)
size = np.zeros(loop)

print(success)
l = 0
for l in range(loop):
    x1 = np.array_split(realpathx,loop)[l]
    y1 = np.array_split(realpathy,loop)[l]
    x1 = x1[x1 != 0]
    y1 = y1[y1 != 0]
    plt.plot(x1, y1, c= np.random.rand(3,))
    
    for n in range(len(x1)):
        averagex[n] += x1[n]
        averagey[n] += y1[n]
        size[n] += 1
    
    
plt.plot(boundaryx, boundaryy, '--r')
plt.show()

averagex = averagex[averagex != 0]
averagey = averagey[averagey != 0]
size = size[size != 0]

averagex = averagex/size
averagey = averagey/size



plt.plot(averagex, averagey, '-b')
plt.plot(boundaryx, boundaryy, '--r')
plt.show()


