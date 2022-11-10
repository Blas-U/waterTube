import numpy as np
import time
from ezGraph import *

#Model
# h = 2t - 3.22


#Parameters
dt = .5
nsteps = 50


# linear model
# m = 5.03
# b = -17.2

r = 2.25 #radius (cm)
Q = 5 # Volume inflow rate: (cubic cm / s)
h = 0



#Graph
graph = ezGraph(xmax = 30,
    ymin=0, ymax=10,
    xLabel="Time (s)",
    yLabel="Height (cm)")

#TIME LOOP
for t in range(nsteps):
  
    modelTime = t * dt

    dh = Q * dt / (np.pi * r **2)
    h = h + dh
    print(modelTime, h)
    graph.add(modelTime, h)
    graph.wait(.1)
    


#draw graph
graph.keepOpen()