#!/usr/bin/env python3
# Exercise 7.2

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from numpy import zeros
from cmath import exp,pi

# Import sunspots dataset.
sunspots = pd.read_csv('sunspots.txt',sep='\t',names=['Month','Sunspots'])

# Create new column for date by using start date specified and month offset.
start            = pd.Timestamp('1749-01-01')
sunspots['Date'] = [start + pd.DateOffset(months=i) for i in sunspots.Month]

# Print observed information about sunspots.
print('Roughly 4 cycles take place in a 40 year period. This means a cycle takes about 10 years or 120 months.')

# Provided dft() function from lectures.
def dft(y):
    N = len(y)
    c = zeros(N//2+1, complex) 
    for k in range(N//2+1):
        for n in range(N): 
            c[k] += y[n]*exp(-2j*pi*k*n/N)
    return c

# Optimized lecture dft function using numpy.
def dftOptimized(y):
    
    # Determine number of elements in y and create numpy arrays.
    N           = len(y)
    halfN       = int(np.floor(N/2) + 1)
    yArray      = np.array(y)
    indexes     = np.arange(0,N)
    coeficients = np.array([np.sum(yArray * np.exp(-2j*np.pi*k*indexes/N)) for k in range(halfN)])

    return coeficients

# Evaluate using dft for graphing.
#values  = dftOptimized(sunspots.Sunspots)**2 #abs, div by N. Check if correct to raise to 2nd.
values  = abs(dftOptimized(sunspots.Sunspots))  #Result seems more reasonable.
                                               # Has frequency spike at 25.
# Abs of complex is a^2 - b^2 although built in np should handle.
                                                
indexes = np.arange(0,len(values))

# Create subplots.
fig, ax = plt.subplots(1, 2)
fig.subplots_adjust(wspace=.5)
fig.set_size_inches(9,5)

# Plot the sunspots over time.
ax[0].plot(sunspots.Date, sunspots.Sunspots,linewidth=0.5)
ax[0].set_title('Monthly Sunspot Count')
ax[0].set_xlabel('Year')
ax[0].set_ylabel('Number of sunspots counted')

# Plot dft graph.
ax[1].plot(indexes, values)
ax[1].set_title('Power')
ax[1].set_xlabel('k - Frequency')
ax[1].set_ylabel('Amplitude')

# Display graphs.
plt.show()

# Display results.
print("The highest frequency occurs as k=25 which corresponds to 100/25 -> 4.")

# Compared to 120 months. - 100 months. ~20 v ~24/25