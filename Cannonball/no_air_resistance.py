#!/usr/bin/env python3
# Cannonball without air resistance

# Reference material
# https://www.omnicalculator.com/physics/projectile-motion (Note units).
# https://phet.colorado.edu/sims/html/projectile-motion/latest/projectile-motion_en.html

import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt


def cannonball_path_in_vacuum(initial_velocity=100, angle_degrees=45):
    '''Track path of cannonball in vacuum with given velocity (meters) and initial angle.'''

    # Local gravity.
    g = 9.81
    angle_radians = np.deg2rad(angle_degrees)  # Multiply degrees by ∏/180°.

    # Calculate initial velocity components.
    velocity_x = initial_velocity * np.cos(angle_radians)
    velocity_y = initial_velocity * np.sin(angle_radians)

    # Calculate time of flight.
    time_of_flight = (2 * velocity_y)/g

    # Calculate distance traveled.
    distance = velocity_x * time_of_flight

    # Create time intervals to make measurements at.
    time_intervals = np.linspace(0, time_of_flight)

    # Generate x and y coordinates.
    x_positions = velocity_x * time_intervals
    y_positions = (-.5*g*(time_intervals**2)) + (velocity_y*time_intervals)

    return x_positions, y_positions, distance


if __name__ == "__main__":

    # Create sample cannonball.
    x_positions, y_positions, distance = cannonball_path_in_vacuum()

    # Plot using plotly
    fig = px.line(x=x_positions, y=y_positions, title='No air resistance (Any mass)')
    fig.show()

    # Matplotlib option plotting (y lim is distance instead of parabola height for square graph).
    plt.plot(x_positions, y_positions, label="'No air resistance (Any mass)'")
    plt.legend()
    plt.xlim(0, distance)
    plt.ylim(0, distance)
    plt.show()
