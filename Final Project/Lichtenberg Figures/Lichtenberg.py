#!/usr/bin/env python3
# Final Project - Lichtenberg Figures

import numpy as np
import Configuration
import Visualization
import Pipeline

# Load configuration file.
configuration_info = Configuration.Configuration()

# Create spacing, needed for correct grid scale automatically.
x_points = np.linspace(0, 1, num=configuration_info.grid_resolution_x_points)
y_points = np.linspace(0, 1, num=configuration_info.grid_resolution_y_points)

# Calculate corresponding offset (needed so pixels are not truncated)
x_offset = x_points[1] / 2.0
y_offset = y_points[1] / 2.0

# Create a meshgrid.
xs, ys = np.meshgrid(x_points, y_points)

# Create a pipeline for performing steps and create initial points.
pipeline_process = Pipeline.Pipeline(configuration_info)

# Create animation.
visualizer = Visualization.Visualization(x_offset, y_offset, configuration_info, pipeline_process)
visualizer.create_animation()