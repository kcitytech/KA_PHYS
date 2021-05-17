#!/usr/bin/env python3
# Runge-Kutta Utility Functions

def runge_kutta_XY(time_points, time_step_size, function, components, mass, stop_zero=True):
    ''' Determine X & Y positions using runge kutta for a given mass.'''

    # Track x & y points using arrays.
    x_points = []
    y_points = []

    # Iterate for time steps.
    for time_step in time_points:

        # Add points to respective array.
        x_points.append(components[0])
        y_points.append(components[2])

        # Utilize function provided in slides.
        k1 = time_step_size * function(components, time_step, mass)
        k2 = time_step_size * function(components + 0.5 * k1, time_step + (0.5 * time_step_size), mass)
        k3 = time_step_size * function(components + 0.5 * k2, time_step + (0.5 * time_step_size), mass)
        k4 = time_step_size * function(components + k3, time_step + time_step_size, mass)
        components += (k1 + 2 * k2 + 2 * k3 + k4) / 6

        # If specified, stop calculations when cannonball impacts ground.
        if stop_zero and y_points[-1] < 0:

            # Truncate to ground since it has already passed through.
            y_points[-1] = 0
            break

    return x_points, y_points
