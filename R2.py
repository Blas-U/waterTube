x_measured = [1,7,12,17,22,26]
y_measured = [0,10,20,30,40,50]
y_modeled = [0.8, 12.8, 22.8, 32.4, 41.8, 51.2]

def avg1(lst):
    return sum(lst)/len(lst)

def res(lst1, lst2):
    n = len(lst1)
    m=0
    for i in range(n):
        # print(i, lst1[i], lst2[i])
        d = lst1[i] - lst2[i]
        m += d**2
    return m

m = res(x_measured, y_measured)
print(m)

def meanDiff(lst):
    n = len(lst)
    d = 0
    a = avg1(lst)
    for i in range(n):
        ave = (lst[i] - a)**2
        d += ave
        print(i, lst[i], d, a)
    return d

mean = meanDiff(y_measured)
print(mean)

r2 = 1-(m/mean)
print (r2)

