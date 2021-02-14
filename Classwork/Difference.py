#!/usr/bin/env python3
# Exercise
# 'difference of two numbers'

import numpy as np

# Create two values to demonstrate ordering difference.
x = 1
y = 1 + 1e-14 * np.sqrt(2)

# Print out to display difference.
print(1e14 * (y-x))
print(np.sqrt(2))