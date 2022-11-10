import numpy as np
import time
from ezGraph import *
from uStats import *


#0.8, 12.8, 22.8, 32.4, 41.8, 51.2
#Modeled is the slope of the line at certain points.

#model is the  the imitation of an original.


# model - a representation of the real world.
#   requites some data about the real world.
#Analytical model: equation or function tht representes (best fits) the data.
#Linear, polynomial, exponention, sinusoidal, logarithmic, hyperbolic, radical.
############################################################################## h(t) = 2 t + 7
#imput: t 
#output: h
#Only waorks for well behaved systems (simple systems). Not a wholle lot of interactions taht will introduce errors.non-chaotic.
#often use calculus to find the equations.
#physical Models
#   small scale physical thing (you can touch it)
#can be more complex
# numerical models
#Usually computer model because there are a lot of calculations. (algabreac calculations)
#usually break the system into smaller parts that interact with each other.
#the coputer is used to keep trach of all the interactions.
# We'll focus on things that chagne over time.
# we'll focus on finite difference models.

#Parameters
dt = 1.
nsteps = 40


# linear model
# m = 5.03
# b = -17.2

r = 2.25 #radius (cm)
Q = 0 # Volume inflow rate: (dv/dt) (cubic cm / s)
h = 50        #initial hight (cm)
k = 1.0     #outflow rate constant

x_measured = [1, 6, 11, 17, 25, 31]
y_measured = [50,40,30,20,10,0]
y_modeled = []


# def avg1(lst):
#     return sum(lst)/len(lst)

# def res(lst1, lst2):
#     n = len(lst1)
#     m=0
#     for i in range(n):
#         d = (lst1[i] - lst2[i]) **2
#         m += d
#         print(i, lst1[i], lst2[i], "sum", m,'res', d)
#     return m

# def meanDiff(lst):
#     n = len(lst)
#     d = 0
#     a = avg1(lst)
#     for i in range(n):
#         ave = (lst[i] - a)**2
#         d += ave
#         print(i, lst[i], d, a)
#     return d
#Model
# h = 2t - 3.22

# def myAvg(lst):
#     return sum(lst)/len(lst)

# def yAvg(lst):
#     return sum(lst)/len(lst)

# def residual(lst):




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

# x = sum(x_measured)/len(x_measured)
    
# print('h_measured:', y_measured)
# print("h_modeled:", y_modeled)

# print(f'xavg measured =  {findAvg(x_measured)}')
# # print(f'yavg measured =  {yAvg(y_measured)}')
# # print(f'Residual' = {resSq(y_measured, y_modeled)})

# # # calculate average values
# m = res(y_modeled, y_measured)
# print("residual",m)

# #draw graph

# mean = meanDiff(y_measured)
# print('sum mean', mean)

# r2 = 1-(m/mean)
# print ("r2", r2)
r2 = rSquared(x_measured, y_modeled)
print(r2)

graph.keepOpen()