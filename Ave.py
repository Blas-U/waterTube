from tkinter import N
import numpy as np
import time

x = [ 3, 5, 22, 11, 7]

def avg1(lst):
    return sum(lst)/len(lst)

avg = avg1(x)
print("AVG1:", avg)
print()


def avg2(lst):
    s = 0
    n = 0
    for i in lst:
        s =+ i 
        n=+1
        return s/n

avg = avg2(x)
print(avg)