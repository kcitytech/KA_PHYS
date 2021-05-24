#!/usr/bin/env python3

import yaml
import numpy as np
import astropy.units as u

class Configuration:
    '''Class to load parameters from yaml file for simulation and animation.'''

    def __init__(self, path='configuration.yaml'):

        # Load the configuration file.
        with open(path, 'r') as configuration_file:

            # Access yaml file data.
            data = yaml.load(configuration_file, Loader=yaml.FullLoader)

        # Access configuration keys
        self.point_to_meter_ratio = data["point_to_meter_ratio"] * u.m
        self.grid_resolution_x_points = data["grid_resolution_x_points"]
        self.grid_resolution_y_points = data["grid_resolution_y_points"]
        self.initial_particles = data["initial_particles"]

        # Compute scale of grid.
        self.physical_size_x_axis = self.grid_resolution_x_points * self.point_to_meter_ratio
        self.physical_size_y_axis = self.grid_resolution_y_points * self.point_to_meter_ratio

        # Initial particle(s) will be stored as a position mask. This may not be used later.
        self.initial_particles_mask = np.zeros((self.grid_resolution_x_points, self.grid_resolution_y_points),dtype=int)
        for point in data["initial_particles"]:
            self.initial_particles_mask[point[0], point[1]] = 1

        # Access animation configuration values.
        self.timesteps = data["timesteps"]
        self.capture_interval = data["capture_interval"]
        self.frame_delay_ms = data["frame_delay_ms"]
        self.repeat_delay_ms = data["repeat_delay_ms"]
        
        # Simulation informaation.
        self.initial_particle_density = data["initial_particle_density"]
        self.stickiness_probability = data["stickiness_probability"]

# Test import
if __name__ == "__main__":

    # Import default location config file.
    configuration_object = Configuration()
    print("Loaded Configuration\n================================")
    print("point_to_meter_ratio:     {}".format(configuration_object.point_to_meter_ratio))
    print("grid_resolution_x_points: {}".format(configuration_object.grid_resolution_x_points))
    print("grid_resolution_y_points: {}".format(configuration_object.grid_resolution_y_points))
    print("physical_size_x_axis:     {}".format(configuration_object.physical_size_x_axis))
    print("physical_size_y_axis:     {}".format(configuration_object.physical_size_y_axis))
    print("timesteps:                {}".format(configuration_object.timesteps))
    print("capture_interval:         {}".format(configuration_object.capture_interval))
    print("frame_delay_ms:           {}".format(configuration_object.frame_delay_ms))
    print("repeat_delay_ms:          {}".format(configuration_object.repeat_delay_ms))
    print("initial_particle_density: {}".format(configuration_object.initial_particle_density))
    print("stickiness_probability:   {}".format(configuration_object.stickiness_probability))
    print("initial_particles:\n\n{}\n".format(configuration_object.initial_particles))
    print("================================")
    
    # Self initial particles array not currently printed.