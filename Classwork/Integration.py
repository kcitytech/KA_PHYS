#!/usr/bin/env python3
# Example 5.1, 5.2, 5.6

import numpy as np

def func(x):
    
    # x^4 -2x +1
    return (x**4)-(2*x)+1

def step(a, b, slices):
    
    # Determine step size.
    return (b-a)/slices
    
def trapezoidal(func, a, b, slices):
    
    # Add the endpoints to the area value.
    area = func(a) + func(b)
    
    # Determine points to use for calculation.
    points = np.linspace(a, b, slices+1, endpoint=True)
    
    # Iterate points skipping endpoints (a & b).
    area += sum([2*func(point) for point in points[1:-1]])
    
    # Multiply area by step size / 2.
    area *= step(a, b, slices)/2
    
    return area

def simpsons(func, a, b, slices):
    
    # Determine points to use for calculation.
    points = np.linspace(a, b, slices+1, endpoint=True)
    
    # Predetermine coefficients which follows form [1 4 2  ... 4 21].
    coefficients = [1] + np.tile([4,2], int(slices/2)).tolist()[:-1] + [1]
    
    # Iterate points to add.
    area = (step(a, b, slices)/3) * sum([coefficient * func(point) for coefficient, point in zip(coefficients, points)])
    
    return area

# Input arguments
a      = 0
b      = 2
slices = 10

# Perform trapezoidal calculation with 10 slices.
print("Trapezoidal method = {:<18} ({:>4} slices)".format(trapezoidal(func, a, b, slices), slices))

# Perform trapezoidal calculation with 100 slices.
slices = 100
print("Trapezoidal method = {:<18} ({:>4} slices)".format(trapezoidal(func, a, b, slices), slices))

# Perform trapezoidal calculation with 1000 slices.
slices = 1000
print("Trapezoidal method = {:<18} ({:>4} slices)".format(trapezoidal(func, a, b, slices), slices))

# Perform Simpson's calculation with 10 slices.
slices = 10
print("  Simpson's method = {:<18} ({:>4} slices)".format(simpsons(func, a, b, slices),slices))

# Perform Simpson's calculation with 100 slices.
slices = 100
print("  Simpson's method = {:<18} ({:>4} slices)".format(simpsons(func, a, b, slices),slices))

# Perform Simpson's calculation with 1000 slices.
slices = 1000
print("  Simpson's method = {:<18} ({:>4} slices)".format(simpsons(func, a, b, slices),slices))

# Calculate error using specified formula
print("Simpson's Error <    {:.20f}".format(abs((1/15)*((simpsons(func, a, b, 20))-simpsons(func, a, b,10)))))