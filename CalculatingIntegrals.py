#!/usr/bin/env python3
# Exercise 4.4: Calculating integrals

import numpy as np

# Specified function.
def f(x):
    return np.sqrt(1 - (x**2))

# y sub k
def yk(h, k):
    return f(xk(h, k))

# x sub k
def xk(h, k):
    return -1 + (h * k)

# Reimann integral using n slices.
def reimannIntegral(n):
    
    # Width of slice
    h = 2/n
    
    # Calculate Reimann integral
    ks = np.arange(1, n+1)
    
    # Calculate value
    value = np.array(h * yk(h, ks)).sum()

    return value

# Run for 100 iterations and 10 million iterations (for total execution time < 1 sec).
integral100    = reimannIntegral(100)
iterations1sec = 10_000_000
integral1sec   = reimannIntegral(iterations1sec)

# Display calculated for for number of iterations.
print("Calculated: {} (100 iterations)".format(integral100))
print("Calculated: {} ({} iterations)".format(integral1sec, iterations1sec))

# Display actual (truncated) value.
print("Actual:     1.57079632679489661923132169163975144209858469968")

# Display results.
print("Using 10 million iterations the value calculated is accurate to 10 decimal places.")