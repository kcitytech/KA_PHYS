#!/usr/bin/env python3
# Exercise 5.15

import numpy as np
import matplotlib.pyplot as plt

# Specified function.
def f(x):
    return 1 + (0.5 * np.tanh(2*x))

# Derivative of function. sech() - equivalent to 1/cosh().
def derivativef(x):
    return (1/np.cosh(2*x))**2

# Central difference function.
def centralDifference(f, x, step):
    return (f(x + (step/2)) - f(x - (step/2))) / step

# Specify range to evaluate and number of samples.
a       = -2
b       = 2
samples = 50

# Calculate step size.
step = (b-a)/(samples-1)

# Calculate values calculated.
xs                = np.linspace(a, b, samples)
functionPoints    = f(xs)
derivativePoints  = derivativef(xs)
centralDiffPoints = centralDifference(f, xs, step)

# Display with plot
plt.figure("Central Difference")
plt.title("Comparison Plot")
plt.plot(xs, functionPoints,    c='b', ls="-",      label="Function")
plt.plot(xs, derivativePoints,  c='r', ls="--",     label="Derivative")
plt.plot(xs, centralDiffPoints, c='g', ls="dotted", label="Central Difference")
plt.legend()
plt.show()