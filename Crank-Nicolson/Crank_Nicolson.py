#!/usr/bin/env python3
# Exercise 9.8: The Schrödinger equation and the Crank–Nicolson method

import astropy.constants as constants
import astropy.units as units
import numpy as np
import Crank_Nicolson_Functions as CNK

# Define mass and box length.
mass = constants.m_e
box_length = 1e-8 * units.m

# Define number of slices and time step.
slices = 1000
time_step = 1e-18 * units.s
grid_step = box_length/slices
x_points = np.linspace(0, box_length, slices, endpoint=False)

# Define electron wavefunction parameters.
x_initial_position = box_length/2
sigma = 1e-10 * units.m
kappa = 5e10 * (units.m**-1)

# Create convenience variable for hbar.
h_bar = constants.hbar

# Define matrix elements.
a_1 = 1 + time_step * ((1j * h_bar)/(2*mass*grid_step**2))
a_2 = -time_step * ((1j * h_bar)/(4*mass*grid_step**2))
b_1 = 1 - time_step * ((1j * h_bar)/(2 * mass * grid_step**2))
b_2 = time_step * ((1j * h_bar)/(4 * mass * grid_step**2))
    
# Create matrixes a & b.
matrix_a = CNK.create_matrix_a(slices, a_1, a_2)
matrix_b = CNK.create_matrix_b(slices, b_1, b_2)
new_phi  = CNK.create_phi_vector_for_position(x_initial_position, x_points, kappa, sigma, matrix_a, b_1, b_2)

# Create a wavefunction animation, save as gif and display.
CNK.create_wavefunction_animation(x_points, kappa, sigma, matrix_a, b_1, b_2)