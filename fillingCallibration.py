import numpy as np
import time
from ezGraph import *

x_measured = [1,7,12,17,22,26]
y_measured = [0,10,20,30,40,50]
y_modeled = [0.8, 12.8, 22.8, 32.4, 41.8, 51.2]


def avg1(lst):
    return sum(lst)/len(lst)

def res(lst1, lst2):
    n = len(lst1)
    m=0
    for i in range(n):
        d = (lst1[i] - lst2[i]) **2
        m += d
        print(i, lst1[i], lst2[i], "sum", m,'res', d)
    return m

def meanDiff(lst):
    n = len(lst)
    d = 0
    a = avg1(lst)
    for i in range(n):
        ave = (lst[i] - a)**2
        d += ave
        print(i, lst[i], d, a)
    return d
#Model
# h = 2t - 3.22

# def myAvg(lst):
#     return sum(lst)/len(lst)

# def yAvg(lst):
#     return sum(lst)/len(lst)

# def residual(lst):



#Parameters
dt = 1.
nsteps = 30


# linear model
# m = 5.03
# b = -17.2

r = 2.25 #radius (cm)
Q = 30 # Volume inflow rate: (dv/dt) (cubic cm / s)
h = 0        #initial hight (cm)
k = 0.0      #outflow rate constant

# x_measured = [1,7,12,17,22,26]
# y_measured = [0,10,20,30,40,50]
# y_modeled = [3.772561614030112, 15.09024645612045, 24.521650491195725, 33.953054526271, 43.38445856134628, 50.9295817894065]

#Graph
graph = ezGraphMM(xmax = 100,
    ymin=0, ymax=100,
    x_measured = x_measured,
    y_measured = y_measured,
    xLabel="Time (s)",
    yLabel="Height (cm)")


graph.addModeled(0,h)

#TIME LOOP
for t in range(nsteps):
  
    modelTime = t * dt

    dh = Q * dt / (np.pi * r **2)
    h = h + dh

    dVdt = -k * h 
    dh = dVdt * dt / (np.pi * r**2)
    h = h + dh

    if (modelTime in x_measured):
        print(modelTime, h)
        y_modeled.append(h)

    graph.addModeled(modelTime, h)
    #graph.wait(.1)

# s = 0
# def
# for i in x_measured:
#     s = s + x_measured
#     Ave = s / s.len
#     print(s)

x = sum(x_measured)/len(x_measured)
    
print('h_measured:', y_measured)
print("h_modeled:", y_modeled)

# print(f'xavg measured =  {myAvg(x_measured)}')
# print(f'yavg measured =  {yAvg(y_measured)}')
# # calculate average values
m = res(y_modeled, y_measured)
print("residual",m)
#draw graph

mean = meanDiff(y_measured)
print('sum mean', mean)

r2 = 1-(m/mean)
print ("r2", r2)

graph.keepOpen()