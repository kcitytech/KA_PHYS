#!/usr/bin/env python3
# Exercise 6.10

import numpy as np
import matplotlib.pyplot as plt

# Create function for equation: x = 1-e^(-cx). Note: e^0 = 1, therefore 0 = 1-[1] is a solution.
def func(x, c):
    return 1-np.exp(-c*x)

# Calculate x for function as well as providing progression of x values.
def relax(c, initialGuess, precision=0.001, maxIterations=10):
    
    # Set inital starting value for x.
    x = [initialGuess]
    
    # Iterate until the value of x seems to converge on a solution.
    for i in range(maxIterations):
        
        # Add found value for function.
        x.append(func(x[-1], c))
        
        # If specified precision is reached, exit loop.
        if abs(x[-1]-x[-2]) <= precision:
            break
    
    # Return the result of x found and intermediate values.
    return x[-1], x
    
# Perform relax() function for range of c values.
def rangeRelax(cs, initialGuess, precision=0.001, maxIterations=10):
    
    # Create an array of determinations for x corresponding to input c.
    xValues = [relax(c, initialGuess, precision, maxIterations)[0] for c in cs]
    return xValues
    
# Perform test of relaxation method.
x0, results0 = relax(2, 0)
x1, results1 = relax(2, 1)
print("Initial guess {}, found x as {} = {}. \n  Steps: {}".format(0, x0, func(x0, 2), results0))
print("Initial guess {}, found x as {} = {}. \n  Steps: {}".format(1, x1, func(x1, 2), results1))
    
# Calculate solution for specified interval of c values.
cs = np.linspace(0, 3, num=30+1)

# Evaluate relax() for range of c values.
xValues = rangeRelax(cs, 1)

# Plot the resulting x values for given c values.
plt.figure('Example 6.1')
plt.suptitle('Relaxation method')
plt.title('$x = 1-e^{-cx}$')
plt.xlabel('c')
plt.ylabel('x')
plt.scatter(cs,xValues)
plt.show()