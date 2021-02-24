#!/usr/bin/env python3
# Exercise 5/12: The Stefan–Boltzmann constant
#
# Note: External file is required to run - gaussxw.py.
# http://www-personal.umich.edu/~mejn/computational-physics/gaussxw.py
#
# Resources:
# https://en.wikipedia.org/wiki/Planck%27s_law - 'Angular frequency'
# https://ps.uci.edu/~cyu/p115A/LectureNotes/Lecture14/html_version/lecture14.html

# TODO: Calculation result is correct however using astropy is resulting in different units.
# Verify units are correct and check for equivalences (and cast).

import numpy as np
import matplotlib.pyplot as plt
from scipy   import constants
from astropy import constants as const
from astropy import units     as u
import gaussxw

# Calculate thermal energy per second given Omega - angular frequency & T - Temperature (Kelvin).
def thermalEnergyPerSecond(omega, T):
    
    # Import physical constants from astropy. Import pi (dimensionless) from numpy.
    hbar = const.hbar
    pi   = constants.pi
    c    = const.c
    kb   = const.k_B
    
    # Apply dimensions to arguments.
    omega *= u.rad / u.s   # TODO: CHECK - Is this dimensionless?
    T     *= u.K # Kelvin
    
    # Create equation using dimensioned constants.
    a = hbar /( 4*(pi**2) * (c**2) )
    b = ( hbar * omega )/( kb * T)
    c = omega**3 / (np.exp(b.value) - 1)
    
    # Combine elements to create equation.
    equation = a * c
            
    return equation

# Define function to integrate.
def f(x):
    return x**3 / (np.exp(x) - 1)

# Integrate using x.
def integrateBlackBodyComponent(x):
    
    # Calculate upperbound to use as minimum iteration.
    upperBoundX = np.log(1_000_000_000)
    
    # Assuming previous integral evaluating from 0 to 2 with 1000 (excessive) iterations.
    a = 0
    b = np.ceil(upperBoundX)*20 # Multiply to exceed upperbound even further.
    N = 1000
    
    # Calculate weights and integration points and sum.
    integrationPoints, weights = gaussxw.gaussxwab(N , a, b)
    result                     = (np.array(weights * f(integrationPoints))).sum()
    
    return result #~6.4939394022668291

def radiatedEnergyBlackBody(x, T):
    
    # Apply units TODO:Need units for x.
    x *= 1
    T *= u.K
    
    # Specify constants.
    kb   = const.k_B
    hbar = const.hbar
    pi   = constants.pi
    c    = const.c
        
    # Create equation.
    a      = ((kb**4)*(T**4)) / (4*(pi**2)*(c**2)*(hbar**3))
    b      = integrateBlackBodyComponent(x)
    result = a * b
            
    return result

# Generate graph visualization.
def visualizeEquation():
    
    # Visualize result to verify equation. Note: Expect reduced performance due to dimensioned constants.
    omegaRange = np.linspace(1, 1e16, num = 1000)
    plt.figure("Planck's Law")
    plt.title("Planck's Law")
    plt.plot([thermalEnergyPerSecond(omega, 5000).value for omega in omegaRange], label="5000K")
    plt.plot([thermalEnergyPerSecond(omega, 4000).value for omega in omegaRange], label="4000K")
    plt.plot([thermalEnergyPerSecond(omega, 3000).value for omega in omegaRange], label="3000K")
    plt.legend()
    plt.show()

# Perform calculation.
def calculateStefanBoltzmannConstant(omega, temperature):

    # Calculate Stefan-Boltzmann constant using arbitrary temperature and omega.
    w                       = radiatedEnergyBlackBody(omega, temperature)
    temperatureTo4thPower   = temperature**4
    stefanBoltzmanConstant  = w/temperatureTo4thPower
    
    return stefanBoltzmanConstant

# Test matches expected.
calculatedValue = calculateStefanBoltzmannConstant(1, 4000)

# Display results. NIST value from https://physics.nist.gov/cgi-bin/cuu/Value?sigma
print("WARNING: TODO: Units returned do not match.")
print("Calculated: {}".format(calculatedValue)) # Fix units.
print("Scipy:      {}".format(const.sigma_sb))
print("NIST:       5.670374419... x 10-8 W m-2 K-4")

# Plot graph to visualize equation.
visualizeEquation()