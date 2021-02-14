#!/usr/bin/env python3
# Exercise
# '0.1 is not represented exactly in binary'

# Create floating point variable b.
b = 0.1

# Display type of variable (float).
print(type(b))

# Print 30 places with 20 after decimal point.
print("{:30.20}".format(b))

# Use sys to find and display computer float type.
import sys
sys.float_info