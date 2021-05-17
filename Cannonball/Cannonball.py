#!/usr/bin/env python3
# Exercise 8.7: Trajectory with air resistance

from astropy import units
from astropy import constants
import numpy as np
import RungeKutta as RK
import CannonballGraphing as CG
import no_air_resistance as vaccuum_cannonball


def make_time_range(stop=10, N=10000):
    ''' Convenience method for time range.'''

    interval = stop/N
    return np.arange(0, stop, interval), interval


def air_resistance_force(mass):
    ''' Air resistance force experienced by cannonball. '''

    # Calculate air resistance. Note must divide by (2*mass) otherwise result will flip.
    return (np.pi * (radius.value ** 2) * air_density.value * coefficient_drag) / (2*mass)


def calculate_values(components, time_step, mass):
    '''Generate values for calculation for each component.'''

    # Compose values by using equations.
    vx = components[1]
    vy = components[3]
    v = np.sqrt(vx**2 + vy**2)
    air_resistance = air_resistance_force(mass)
    values = np.array([vx, -air_resistance * vx * v, vy, -g.value - air_resistance * vy * v])

    return values


def cannonball_xy_positions(time_points, time_step_size, mass, stop_zero=True):
    ''' Determine xy trajectory for a spherical object with a given mass.'''

    # Determine base conditions for components prior to iteration.
    a = initial_velocity.value * np.cos(angle_radians)
    b = initial_velocity.value * np.sin(angle_radians)
    components = np.array([0, a, 0, b])

    # Calculate the XY positions of the spherical body.
    xs, ys = RK.runge_kutta_XY(time_points, time_step_size, calculate_values, components, mass, stop_zero)

    return xs, ys


def positions_for_masses(masses, time_points, time_step_size):
    ''' Create dictionary to link positions by mass key. '''

    # Create dictionary to show masses and corresponding coordinates.
    mass_positions = {}

    # Iterate masses to create a dictionary of x,y coordinates.
    for mass in masses:

        # Create cannonball and calculate xy positions.
        xs, ys = cannonball_xy_positions(time_points, time_step_size, mass)
        formatted_mass = "{} kg".format(mass)

        # Add the coordinates to dictionary for mass.
        mass_positions[mass] = {"formatted_mass": formatted_mass, "xs": xs, "ys": ys}

    return mass_positions


if __name__ == "__main__":

    # Define constants specified for cannonball.
    air_density = 1.22 * (units.kg * (units.meter**-3))
    coefficient_drag = 0.47  # Unitless since coefficient.
    initial_velocity = 100 * (units.m/units.s)
    radius = 0.08 * units.m  # Must convert from cm to meters for equation.
    g = constants.g0  # Gravitational constant.
    angle = 30  # 30°
    angle_radians = np.deg2rad(angle)

    # Create a time step size and interval with defaults.
    time_points, time_step_size = make_time_range(stop=10, N=10000)

    # Create cannonballs with sample masses.
    masses = [0.01, 0.1, 1, 2, 4, 100, 10000]

    # Create dictionary of positions for specified masses.
    mass_positions = positions_for_masses(masses, time_points, time_step_size)

    # Create reference cannonball with same initial parameters except no air resistance (mass independent).
    vaccuum_ball_xs, vaccuum_ball_ys, distance = vaccuum_cannonball.cannonball_path_in_vacuum()
    vacuum_dictionary = {"xs": vaccuum_ball_xs, "ys": vaccuum_ball_ys}

    # Create title for graphs.
    title = "Cannonballs after ~{} seconds.".format(np.ceil(time_points[-1]))

    # Plot using plotly.
    CG.create_plotly_graph(mass_positions, vacuum_dictionary, title=title)

    # Plot using matplotlib.
    CG.create_matplotlib_graph(mass_positions, vacuum_dictionary, title=title)
