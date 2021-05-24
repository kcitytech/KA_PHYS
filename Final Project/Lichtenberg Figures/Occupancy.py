#!/usr/bin/env python3

import numpy as np

def create_occupancy_mask_from_configuration_values(x_points, y_points, initial_particles):

    # Create an occupancy mask for each possible position.
    occupancy_mask = np.zeros((x_points, y_points))

    # Add the initial particles using 1 to represent particle.
    for particle_coordinate in initial_particles:
        occupancy_mask[particle_coordinate[0], particle_coordinate[1]] = 1

    # Reshape array to use in pipeline.
    reshaped_occupancy_mask = np.reshape(occupancy_mask, x_points*y_points)

    return reshaped_occupancy_mask

if __name__ == "__main__":

    # Test out occupancy map
    x_points = 3
    y_points = 3
    initial_particles = [[2,0], [1,1]]
    occupancy_mask    = create_occupancy_mask_from_configuration_values(x_points, y_points, initial_particles)
    assert(np.array_equal(np.array([0,0,0,0,1,0,1,0,0]), occupancy_mask))
    print("OK")