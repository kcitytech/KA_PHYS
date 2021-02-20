#!/usr/bin/env python3
# Example 5.2 - Gaussxw
# Note: External file is required to run - gaussxw.py.
# http://www-personal.umich.edu/~mejn/computational-physics/gaussxw.py

import gaussxw
import numpy as np

# Define specified function.
def f(x):
    return x**4 - (2*x) + 1

# Assuming previous integral evaluating from 0 to 2 with 1000 (excessive) iterations.
a = 0
b = 2
N = 10

# Calculate weights and integration points.
integrationPoints, weights = gaussxw.gaussxwab(N , a, b)

# Calculate result by summing.
result = (np.array(weights * f(integrationPoints))).sum()

# Display results
print("Value: {}".format(result))