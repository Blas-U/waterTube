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

l = 5 #radius (cm)
w = 10
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

    dh = Q * dt / (l * w)
    h = h + dh
    print(modelTime, h)
    graph.add(modelTime, h)
    graph.wait(.1)
    


#draw graph
graph.keepOpen()