#!/usr/bin/env python3

import numpy as np

# Specify constants.
b  = 0.01
hf = 1

# Specify number of iterations.
iterations = 1000000

# Define energy level for given n.
def en(n):
    return hf*(n+(1/2))

def QHO(iterations):

    # Create numpy array of indexes for number of iterations.
    index = np.arange(0, iterations)

    # Calculate corresponding energy levels.
    energyLevels = en(index)

    # Compute Z using numpy array.
    ZArray    = np.exp( -b * energyLevels )
    ZArraySum = ZArray.sum()
    
    # Calculate average energy.
    averageEnergy = (1/ZArraySum) * (energyLevels * ZArray).sum()
    
    # Display the average energy.
    print("Average Energy = {:15.15} ({} iterations)".format(averageEnergy,iterations))
        
# Evaluate for specified number of iterations.
[QHO(iterations) for iterations in [1_000, 1_000_000, 1_000_000_000]]