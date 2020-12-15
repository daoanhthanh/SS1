from __future__ import division, print_function, unicode_literals
import numpy as np 
import matplotlib.pyplot as plt



_range = 100
def derv(x):
    return (-5*np.sin(x) +6*x)

def origin(x):
    return (5*np.cos(x) + 3*x**2)

def GD1(step, x0):
    x = [x0]
    for i in range(_range):
        temp = x[-1] - step * derv(x[-1])
        if abs(derv(temp)) < 1e-3:
            break
        x.append(temp)
    return (x, i)

(x1, i1) = GD1(.1, -5)
(x2, i2) = GD1(.4, 5)
print('Solution x1 = %f, cost = %f, obtained after %d iterations'%(x1[-1], origin(x1[-1]), i1))
