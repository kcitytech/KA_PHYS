#!/usr/bin/env python3
# Exercise 4.2

# Use cmath instead of numpy to allow negative square roots.
import cmath
import numpy as np

def quadratic(a,b,c):
    
    # Calculate results using quadratic formula, alternate form, and using np.
    x1  = (-b + cmath.sqrt( (b**2)-(4*a*c)) ) / (2*a)
    x2  = (-b - cmath.sqrt( (b**2)-(4*a*c)) ) / (2*a)
    xa1 = (2*c) / ( -b + cmath.sqrt( (b**2)-(4*a*c) ))
    xa2 = (2*c) / ( -b - cmath.sqrt( (b**2)-(4*a*c) ))
    xb  = np.roots([a,b,c])
        
    # Min/Max for ordering results will not work if numbers are complex.
    if any(np.iscomplex([x1,x2])):

        # Display roots by extracting real component (no complex part).
        print("Roots-Standard Formula:  {:.12} {:.12}".format(x1,x2))
        print("Roots-Alternate Formula: {:.12} {:.12}".format(xa1,xa2))
        print("Roots-Numpy:             {:.12} {:.12}".format(xb[0],xb[1]))

    else:
    
        # Display roots by extracting real component (no complex part).
        print("Roots-Standard Formula:  {:.12} {:.12}".format(min(x1.real ,x2.real) ,max(x1.real,x2.real)))
        print("Roots-Alternate Formula: {:.12} {:.12}".format(min(xa1.real,xa2.real),max(xa1.real,xa2.real)))
        print("Roots-Numpy:             {:.12} {:.12}".format(min(xb.real)          ,max(xb.real)))
    
# Demonstrate with provided values.
print("Solution for a=0.001, b=1000, c=0.001:")
quadratic(0.001, 1000, 0.001)

# Prompt user for values.
a = float(input('a:'))
b = float(input('b:'))
c = float(input('c:'))

# Display solution.
quadratic(a, b, c)

# The same value for x is not given by different methods in some cases.
# This is a result of machine precision playing a significant role for more extreme values.
# The order of operations also plays a part in magnifying this.