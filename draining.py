from calendar import c
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
a = .9921
b = -3.8
c= 53.5



#Graph
graph = ezGraph(xmax = 30,
    ymin=0, ymax=50,
    xLabel="Time (s)",
    yLabel="Height (cm)")

#TIME LOOP
for t in range(nsteps):
  
    modelTime = t * dt
    h = c * a ** modelTime + b
    print(modelTime, h)
    graph.add(modelTime, h)
    graph.wait(.1)
    


#draw graph
graph.keepOpen()