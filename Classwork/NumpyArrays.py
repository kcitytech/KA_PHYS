#!/usr/bin/env python3
# Exercise 2.8

import numpy as np

# Define two numpy arrays of type int.
a = np.array([1,2,3,4], int)
b = np.array([2,4,6,8], int)

# Divide b by a then add 1 to the result.
print(b/a+1)

# Divide b by the sum of a and 1.
print(b/(a+1))

# Perform integer division (no decimal) of b divided by the sum of a and 1.
print(b//(a+1))