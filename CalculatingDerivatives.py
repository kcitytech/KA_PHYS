#!/usr/bin/env python3
# Exercise 4.3

import matplotlib.pyplot as plt
import numpy as np
import argparse

# Define specified function.
def func(x):
    return x*(x-1) # Equivalent to x^2 - x

# Manually calculated derivative of specified function.
def funcDerivative(x):
    return (2*x) - 1 # x^2 - x -> 2x-1

# Approximate derivative at point x for function using delta (should be small).
def approximateDerivative(func, x, delta):
    return (func(x + delta)-func(x))/delta

# Determine errors in approximations compared to true value.
def errorsForApproximation(approximation, x):
    
    # Calculate errors in approximation (difference of approximation and true values).
    true   = funcDerivative(x)
    errors = abs(approximation - true)
    return errors

# Plot deltas with errors.
def plot(deltas, errors):
    
    # Graph error corresponding to delta values with grid to show distinct jumps.
    fig = plt.figure("Calculating Derivatives")
    ax  = fig.gca()
    ax.grid()
    
    # Flip graph horizontally to show error initially decreasing with smaller delta.
    ax.set_xlim(deltas[0], deltas[-1])
    
    # Plot deltas vs errors.
    plt.title("Plot f({}) derivative".format(1))
    plt.plot(deltas, errors)
    plt.xlabel(r"$\Delta$ - Delta")
    plt.ylabel(r"$\epsilon$ - Error")
    plt.xscale('log')
    plt.yscale('log')
    plt.show()

# Print output for approximation given specified x and delta.
def displayApproximationInformation(x, delta):

    # Calculate derivative using specified x and delta values.
    approximation = approximateDerivative(func, x, delta)
    actualStored  = funcDerivative(x)
    
    # Display approximated value.
    print("\nDerivative at x = {} delta = {}: (truncated)\n".format(x, delta))
    print("\tApproximation: {:8f}".format(approximation))
    print("\tActual Stored: {:8f}\n".format(actualStored))

    # Provide explanationatory text.
    print('''NOTE: Expect approximation to differ significantly with large delta. Reducing delta will result in improved accuracy until a point at which error will compound due to machine precision.\n''')

# Display graph comparing deltas and corresponding errors.
def displayComparisonGraph(x, deltas):

    # Create aproximation and determine corresponding errors.
    approximations = approximateDerivative(func, x, deltas)
    errors         = errorsForApproximation(approximations, x)

    # Plot deltas vs errors.
    plot(deltas, errors)
    
if __name__ == "__main__":
    
    print("Example 4.3")
    
    # Create parser to pass in x and delta.
    parser = argparse.ArgumentParser(description = "Point derivative calculator (x²-x).")
    parser.add_argument('--x',     type = float, help='Value to calculate derivative at.')
    parser.add_argument('--delta', type = float, help='Delta to use for calculating derivative.')
    args = parser.parse_args()

    # Specify default x and delta.
    x     = 1
    delta = 1e-2
    
    # Use passed in x if specified.
    if args.x is not None:
        x = args.x
        
    # Use passed in delta if specified.
    if args.delta is not None:
        delta = args.delta
            
    # Calculate approximation for specified value.
    displayApproximationInformation(x, delta)
    
    # Generate graphs showing lab requirement deltas and in class requirement.
    deltasA = np.array([1e-4, 1e-6, 1e-8, 1e-10, 1e-12, 1e-14])
    deltasB = np.power(10, np.linspace(-4, -14, num=50))
    
    # Display explanation prior to graphing..
    print('''Graphs displayed show as delta decreases error will correspondingly decrease. 
    When delta becomes to small error will increase due to accumulation of errors due to machine precision.''')
    
    # Display comparison graphs.
    displayComparisonGraph(1, deltasA)
    displayComparisonGraph(1, deltasB)