#!/usr/bin/env python3

import numpy as np
import Configuration
import Adjacency
import Occupancy
import Particles

class Pipeline:

    def __init__(self, configuration_info):

        # Create reproducible results when drawing for random values.
        np.random.seed(0)

        # Determine number of particles to create.
        self.x_points               = configuration_info.grid_resolution_x_points
        self.y_points               = configuration_info.grid_resolution_y_points
        self.total_grid_positions   = self.x_points * self.y_points
        self.particle_count         = int(configuration_info.initial_particle_density * self.total_grid_positions)
        self.stickiness_probability = configuration_info.stickiness_probability

        # Create free particles mask.
        self.free_particles_mask = Particles.create_free_particles_mask(self.total_grid_positions, self.particle_count)

        # Create mask for initial particles (particles specified in configuration file).
        initial_particles = configuration_info.initial_particles
        self.occupancy_mask = Occupancy.create_occupancy_mask_from_configuration_values(self.x_points, self.y_points, initial_particles)

        # Display the initial particles specified by configuration file.
        figure_layer_occupancy_mask = np.reshape(self.occupancy_mask, (self.x_points, self.y_points))
        self.figure_layer = figure_layer_occupancy_mask

    def execute_numpy_pipeline(self):

        # Perform random walk for particles.
        self.free_particles_mask, self.occupancy_mask = Particles.random_walk_particles(self.free_particles_mask, self.occupancy_mask, 
                                                                                        self.x_points, self.y_points, self.stickiness_probability)
        # Create layer to show occupancy and display.
        figure_layer_occupancy_mask = np.reshape(self.occupancy_mask, (self.x_points, self.y_points))
        self.figure_layer = figure_layer_occupancy_mask

if __name__ == "__main__":
    
    # Access configuration info and run to test.
    configuration_info = Configuration.Configuration()
    lichtenberg_pipeline = Pipeline(configuration_info)
    lichtenberg_pipeline.execute_numpy_pipeline()