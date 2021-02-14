#!/usr/bin/env python3
# Exercise
# 'Find the machine precision of your computer'.

# Find the point at which x+eps is indistinguishable from x.
x   = 1.0
eps = 1.0

# Reduce eps by half every iteration until x+eps is indistinguishable from x.
while not x+eps == x:
    eps = 0.5*eps
    
# Print the value of eps * 2.
print(2*eps)