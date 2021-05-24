#!/usr/bin/env python3

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import Configuration

class Visualization:

    def __init__(self, x_offset, y_offset, configuration_info, pipeline_process):
                
        # Store parameters and generate plot.
        self.configuration_info = configuration_info
        self.pipeline_process = pipeline_process
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.create_plot()
        
    # Later move phys args to config object.
    def create_plot(self):
    
        # Provide some information on render.
        configuration_object = Configuration.Configuration()
        format_string = "(particle density: {} stickiness probability: {})".format(configuration_object.initial_particle_density,configuration_object.stickiness_probability)

        # Create a figure for lichtenberg animation.
        self.fig = plt.figure("Lichtenberg Figure", figsize=(6,6))
        self.ax = self.fig.add_subplot(1, 1, 1)
        self.ax.set_xlim([0,1])
        self.ax.set_ylim([0,1])
        self.ax.axis('square')
        plt.gca().set_aspect('equal')
        plt.gca().set_xlim(0-self.x_offset, 1+self.x_offset)
        plt.gca().set_ylim(0-self.y_offset, 1+self.y_offset)
        self.ax.set_xlabel('{}'.format(self.configuration_info.physical_size_x_axis))
        self.ax.set_ylabel('{}'.format(self.configuration_info.physical_size_y_axis))
        self.ax.set_title(format_string)

    # Animation frame.
    def animate_electric(self, i):
        
        # Random movement.
        self.pipeline_process.execute_numpy_pipeline()
        
        # Generate new grid and update image.
        new_grid = self.pipeline_process.figure_layer
        self.image.set_data(new_grid)

        return self.image
    
    # Create animation.
    def create_animation(self):

        # Baseline image create
        initial_grid = self.pipeline_process.figure_layer
        extent_parameters = [0-self.x_offset, 1+self.x_offset, 0-self.y_offset, 1+self.y_offset]
        self.image = self.ax.imshow(initial_grid, extent=extent_parameters, cmap="plasma", interpolation='None')
        
        # Create animation.
        lichtenberg_figure_animation = animation.FuncAnimation(self.fig, self.animate_electric, 
             interval=self.configuration_info.frame_delay_ms, repeat_delay=self.configuration_info.repeat_delay_ms, frames=100)
        lichtenberg_figure_animation.save('gifs/lichtenberg.gif')

        # Display animation.
        plt.show()