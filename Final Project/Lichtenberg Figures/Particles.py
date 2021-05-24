#!/usr/bin/env python3

import numpy as np
import Adjacency
import Random_Walk

def create_free_particles_mask(total_grid_positions, particle_count):
    ''' Walker particles. '''
    
    # Create a 1D array of randomly distributed free particles by randomly shuffling.
    empty_positions  = np.zeros(total_grid_positions-particle_count)
    filled_positions = np.ones(particle_count)

    # Create a random mask of particles by randomly shuffling empty and filled positions.
    free_particles_mask = np.concatenate((empty_positions, filled_positions))
    np.random.shuffle(free_particles_mask)

    return free_particles_mask

def create_stickiness_mask(occupancy_mask, x_points, y_points, stickiness_probability):

    # Determine positions where particles already occupy positions.
    occupancy_by_rows = np.reshape(occupancy_mask, (x_points, y_points))

    # Create a mask representing where particles can join Lichtenberg Figure.
    adjacency_mask = Adjacency.create_adjacency_mask(x_points, y_points, occupancy_by_rows)

    # Create a mask to determine whether particle will stick at any of these points.
    total_grid_positions = x_points*y_points
    stickiness_probability = np.random.choice(2, total_grid_positions, p=[1-stickiness_probability, stickiness_probability])
    stickiness_mask = adjacency_mask * stickiness_probability

    return stickiness_mask

def random_walk_particles(free_particles_mask, occupancy_mask, x_points, y_points, stickiness_probability):

    # WARNING: Investigate further, possibly variables are passed by value here as causing side effects without np.copy() internally.
    # Generate new free particles and occupancy mask by recomputing.
    free_particles_mask = Random_Walk.inefficient_random_walk(free_particles_mask, occupancy_mask, x_points, y_points)

    # # Create a stickiness mask., 
    stickiness_mask = create_stickiness_mask(occupancy_mask, x_points, y_points, stickiness_probability)

    # # If a particle aligns with the stickiness mask it will become captured and join the figure.
    captured_particles_mask = np.logical_and(free_particles_mask.astype(int), stickiness_mask).astype(int)

    # # Add the captured particles to the occupancy mask normalizing to 1.
    occupancy_mask = occupancy_mask + captured_particles_mask
    occupancy_mask[occupancy_mask > 1] = 1 

    # # Remove captured particles from free particles
    free_particles_mask = free_particles_mask - captured_particles_mask

    return free_particles_mask, occupancy_mask
