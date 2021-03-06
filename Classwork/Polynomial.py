#!/usr/bin/env python3
# Exercise 6.15

import matplotlib.pyplot as plt
import numpy as np

# Define specified equation.
def p(x):
    return (924*(x**6)) - (2772*(x**5)) + (3150*(x**4)) - (1680*(x**3)) + (420*(x**2)) - (42*x) + 1

# Define derivative of specified equation.
def pPrime(x):
    return (5544*(x**5)) - (13860*(x**4)) + (12600*(x**3)) - (5040*(x**2)) + (840*x) - 42

# Define internal method for improving readability.
def newtonsInternal(f, fPrime, xn):
    return (xn - (f(xn)/fPrime(xn)))

# Newton's method.
def newtons(f, fPrime, x0, precision=0.001, maxIterations=100):
    
    # Start with x0 specified and calculated x1 and x2.
    x1 = newtonsInternal(f, fPrime, x0)
    x2 = newtonsInternal(f, fPrime, x1)
    xs = [x1, x2]
    
    # Iterate to find better result for x
    while abs(xs[-1]-xs[-2]) > precision and len(xs) < maxIterations:
        xs.append(newtonsInternal(f, fPrime, xs[-1]))

    # Return last value.
    return xs[-1]

# Create point to evaluate function at to find approximate roots.
xs = np.linspace(0, 1, num=1000)

# Plot interval from 0 to 1 to find approximate roots visually along with y=0.
plt.figure('Exercise 6.15')
plt.title('924x⁶ - 2772x⁵ + 3150x⁴ - 1680x³ + 420x² - 42x +1')
plt.xlabel('x')
plt.ylabel('y')
plt.plot(xs,p(xs))
plt.plot(xs,np.zeros(1000))
plt.show()

# Approximate roots from visual inspection of graph.
# x0 = 0.003
# x1 = 0.165
# x2 = 0.380
# x3 = 0.615
# x4 = 0.830
# x5 = 0.966

# Evaluate to find roots using values found visually.
visualRoots = {'x0':0.003, 'x1':0.165, 'x2':0.380, 'x3':0.615, 'x4':0.830, 'x5':0.966}
newtonRoots = [newtons(p, pPrime, visualRoots[root]) for root in visualRoots]
print("Roots calculated using Newton's method: {}".format(newtonRoots))
print("Actual Approximate Roots:\
0.0337652428984239860938492 \
0.1693953067668677431693002 \
0.3806904069584015456847491 \
0.6193095930415984543152509 \
0.8306046932331322568306998 \
0.9662347571015760139061508")