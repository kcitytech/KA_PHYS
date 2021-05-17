#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def electron_wavefunction_phi(x_current_position, x_initial_position, kappa, sigma):
    '''Wavefunction of the electron for given parameters.'''
    fraction = ((x_current_position-x_initial_position)**2)/(2*sigma**2)
    return np.exp(-fraction)*np.exp(1j*kappa*x_current_position)

def phi_times_matrix_b(phi, b_1, b_2):
    '''Function to find vector for matrix_b * phi_vector. 
       The equation vi = b1ψi + b2(ψi+1 + ψi−1). allows to calculate using
       b_1 and b_2 instead of needing matrix_b. Note: See updated page, prior
       version had incorrect subscript. Note that instructions allow for 
       special formula to be used to avoid needing to use matrix_b.'''

    # Create a vector v.
    vector_v = []
    
    # Iterate through each element in phi to
    for i in range(len(phi)):
        
        # Access the corresponding element of phi vector at index.
        phi_i = phi[i]
        
        # Access next and previous index. WARNING: Assume to ignore if out of range.
        phi_i_plus_1 = 0
        phi_i_minus_1 = 0
        
        # If this is not the last element, then set the next phi value.
        if i < len(phi)-1:
            phi_i_plus_1 = phi[i+1]
            
        # If this is not the first element, set the previous phi value.
        if i > 0:
            phi_i_minus_1 = phi[i-1]
            
        # Create the ith element of the vector v from components.
        vector_i = (b_1*phi_i) + (b_2*(phi_i_plus_1+phi_i_minus_1))
        
        # Add the ith element to the vector v.
        vector_v.append(vector_i)
        
    return vector_v

def phi_vector_for_time_position(x_position, x_points, kappa, sigma):
    '''Create phi vector for a given x_position.'''
    
    # Calculate wavefunction phi for x_points, casting as real as given in instructions.
    phi_vector = electron_wavefunction_phi(x_points, x_position, kappa, sigma)
    phi_vector = np.real(phi_vector)
    
    # Create vector. Instructions specify 'ψ = 0 on the walls at x = 0 and x = L'.
    phi_vector[0] = 0 # x = 0
    phi_vector[-1] = 0 # x = L
    
    return phi_vector

def create_matrix_a(slices, a_1, a_2):
    '''Create matrix a.'''
    
    # Create matrix A and assign a_1 and a_2 to diagonals using using list slicing.
    matrix_a = np.zeros([slices, slices], dtype=complex)
    np.fill_diagonal(matrix_a, a_1)
    np.fill_diagonal(matrix_a[1:], a_2)
    np.fill_diagonal(matrix_a[:,1:], a_2)
    
    return matrix_a

def create_matrix_b(slices, b_1, b_2):
    '''Create matrix b.'''
    
    # Create matrix B and assign b_1 and b_2 to diagonals using using list slicing.
    matrix_b = np.zeros([slices,slices],dtype=complex)
    np.fill_diagonal(matrix_b, b_1)
    np.fill_diagonal(matrix_b[1:], b_2)
    np.fill_diagonal(matrix_b[:,1:], b_2)
    
    return matrix_b

def create_phi_vector_for_position(x_position, x_points, kappa, sigma, matrix_a, b_1, b_2):
    '''Create new phi vector for position.'''
    
    # Generate phi vector
    phi_vector = phi_vector_for_time_position(x_position, x_points, kappa, sigma)
    
    # Create the vector v.
    vector_v = phi_times_matrix_b(phi_vector, b_1, b_2)
    
    # Solve for the new value of phi (using numpy library instead of banded.py).
    new_phi = np.linalg.solve(matrix_a, vector_v)
    
    # Since the wave function is always real the values don't need to be complex (imaginary).
    new_phi = np.real(new_phi)
    
    return new_phi

def create_wavefunction_animation(x_points, kappa, sigma, matrix_a, b_1, b_2):
    ''' Create wavefunction animation.'''
    
    # Create plot for particle motion.
    plt.style.use("Solarize_Light2")
    fig, ax = plt.subplots()
    ax.set_title("Wavefunction")
    ax.set_xlabel("Position (Meters)")
    
    # Create a list to hold lists of images.
    images = []
    
    # Track the iteration to avoid drawing too much.
    iteration = 0
    
    # Iterate for number of desired iterations.
    for x_point in x_points:
        
        # Only generate every 5 frames.
        if iteration % 5 == 0:
            
            # Create phi vector and add graph.
            new_phi = create_phi_vector_for_position(x_point, x_points, kappa, sigma, matrix_a, b_1, b_2)
            image = ax.plot(x_points, new_phi, c='m',linewidth=.5)
            images.append(image)
            
        # Increment iteration
        iteration = iteration + 1
    
    # Reverse images to plot in reverse (removing first and last object which are duplicated).
    images = images + images[::-1][1:-1]
    
    # Create an animation with generated images.
    wavefunction_animation = animation.ArtistAnimation(fig, images, interval=100, blit=True, repeat_delay=10)
    wavefunction_animation.save("wavefunction.gif")
    
    # Display graph.
    plt.show()