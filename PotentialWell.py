#!/usr/bin/env python3
# Exercise 6.14
# Note: Description not yet provided in readme.

import numpy as np
import matplotlib.pyplot as plt
import astropy.units as units
import astropy.constants as constants

# V ___         ___    # w: Width of well   (in nm)
#      |       |       # m: Mass            (in kg)
#    E |-------|       # E: Energy
#      |       |       # V: Voltage         (in eV)
# 0 ___|_______|___    # ħ: Planck constant (in J s)
#      <---w--->


def schrodingerBaseEquation(energy, wellWidthNanometers=1e-9):
    '''Schrodinger equation common to both energy states.'''

    # Convert units. Electron voltes to joules, Meters to nanometers.
    energy = (energy * units.eV).to(units.J)
    wellWidthNanometers *= units.meter

    # Calculate base equation for even and odd states.
    h = constants.hbar
    mass = constants.m_e
    inside = (wellWidthNanometers**2 * mass * energy)/(2 * (h**2))
    result = np.tan(np.sqrt(inside.value))

    return result


def schrodingerEven(V, E):
    '''Equivalent allowed energy equation for even numbered states.'''
    return np.sqrt((V-E)/E)


def schrodingerOdd(V, E):
    '''Equivalent allowed energy equation for odd numbered states.'''
    return np.sqrt(E/(V-E))


def validatePoints(start, end, schrodingerFunction, voltage=20):
    '''Validate binary search endpointspoints for schrodinger function.'''

    # Determine values for start and end.
    x1 = schrodingerBaseEquation(start) - schrodingerFunction(voltage, start)
    x2 = schrodingerBaseEquation(end) - schrodingerFunction(voltage, end)

    # Ensure signs are opposite.
#    if x1/abs(x1) == x2/abs(x2):
#        raise ValueError("Start/end point must evaluate with opposite signs.")


def binarySearch(start, end, schrodingerFunction, voltage=20, accuracy=0.001):
    '''Define binary search/bisection function.'''

    # Validate points
    validatePoints(start, end, schrodingerFunction, voltage=voltage)

    # Continue iterating until solution is found.
    while abs(start-end) > accuracy:

        # Calculate midpoint and corresponding x prime.
        midpoint = (start+end)/2
        startValue = schrodingerBaseEquation(start) - schrodingerFunction(voltage, start)
        midpointValue = schrodingerBaseEquation(midpoint) - schrodingerFunction(voltage, midpoint)
        endValue = schrodingerBaseEquation(end) - schrodingerFunction(voltage, end)

        # Determine if values have the same sign.
        if (startValue/abs(startValue) == midpointValue/abs(midpointValue)):

            # Start can be replaced by midpoint since the sign is the same.
            start = midpoint
        elif (endValue/abs(endValue) == midpointValue/abs(midpointValue)):

            # End can be replaced by midpoint since the sign is the same.
            end = midpoint
        else:
            raise ValueError("Error: Logical assertion violated.")

    return midpoint


# Main
if __name__ == "__main__":

    print("Exercise 6.14")

    # Define voltage and energy range (small offset prevents division by 0).
    voltage = 20 * units.eV
    energyRange = np.linspace(0+.01, 20-.01, num=200)

    # Evaluate equations specified. NOTE: Equation for y3 is negated.
    y1 = schrodingerBaseEquation(energyRange)
    y2 = schrodingerEven(voltage.value, energyRange)
    y3 = - schrodingerOdd(voltage.value, energyRange)

    # Use estimated even/odd x intersections to find y solutions.
    evenSolutions = np.array([0.75, 4.5, 7.84])
    oddSolutions = np.array([1.27, 5.0, 11.2])

    evenSolutionsY = schrodingerEven(voltage.value, evenSolutions)
    oddSolutionsY = -schrodingerOdd(voltage.value, oddSolutions)

    # Graph 3 equations and estimated solutions for first 6 energy levels.
    plt.figure('Energy Levels')
    plt.title('Schrodinger Equations')
    plt.xlabel('Ev')
    plt.plot(energyRange, y1, label='Y1: Base')
    plt.plot(energyRange, y2, label='Y2: Even')
    plt.plot(energyRange, y3, label='Y3: Odd')
    plt.scatter(evenSolutions, evenSolutionsY, c='red', label='Even solutions')
    plt.scatter(oddSolutions, oddSolutionsY, c='cyan', label='Odd solutions')
    plt.legend()
    plt.show()

    # Use binary search to find first 6 energy levels (accurate to 0.001eV).
    level0 = binarySearch(0.68, 0.76, schrodingerEven)
    level1 = binarySearch(1.10, 1.26, schrodingerOdd)
    level2 = binarySearch(4.40, 4.60, schrodingerEven)
    level3 = binarySearch(5.05, 5.10, schrodingerOdd)
    level4 = binarySearch(7.50, 9.00, schrodingerEven)
    level5 = binarySearch(11.00, 11.25, schrodingerOdd)
    levels = [level0, level1, level2, level3, level4, level5]

    # Print out energy levels. Note: Display eV cast from joules.
    print("Energy Levels: {}".format(levels))
    