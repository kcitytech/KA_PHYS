#!/usr/bin/env python3
# 10.3 Brownian Motion

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import argparse


def randomDirection(single_axis_movement=True):
    '''Returns list of direction of travel in x and y direction.'''

    if single_axis_movement:

        movements = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        movement = movements[np.random.randint(0, 4)]
        return movement
    else:
        return np.random.choice([-1, 1], 2)


def grid(x, y):
    '''Generate 2D grid of specified x and y as shaped nparrays of zeros.'''

    return np.zeros(x*y, int).reshape((x, y))


def initialPosition(gridLattice):
    '''Determine initial position for a grid.'''

    shape = gridLattice.shape
    xMidpoint = shape[0] // 2
    yMidpoint = shape[1] // 2
    return xMidpoint, yMidpoint


def is_valid_movement(x_position, y_position, x_delta, y_delta, grid_lattice):
    '''Determine whether movement in x & y directions are allowed.'''

    x_axis_size = grid_lattice.shape[0]
    y_axis_size = grid_lattice.shape[1]
    is_valid_x_movement = is_valid_movement_axis(x_position, x_delta, x_axis_size)
    is_valid_y_movement = is_valid_movement_axis(y_position, y_delta, y_axis_size)
    is_valid = is_valid_x_movement and is_valid_y_movement

    return is_valid


def is_valid_movement_axis(position, movement, axis_length):
    '''Determine whether movement of particle is allowed.'''

    # Calculate the new position.
    new_position = position + movement
    is_valid_axis_movement = new_position >= 0 and new_position <= axis_length-1
    return is_valid_axis_movement


def updateGrid(xPosition, yPosition, gridLattice, is_single_axis_movement):
    '''Provides updated positions and grid lattice for a random movement.'''

    # Calculate new movement.
    x_delta, y_delta = randomDirection(single_axis_movement=is_single_axis_movement)

    while not is_valid_movement(xPosition, yPosition, x_delta, y_delta, gridLattice):
        x_delta, y_delta = randomDirection()

    # Update position with validated movement.
    xPosition += x_delta
    yPosition += y_delta

    # Increment at point for heatmap style.
    gridLattice[xPosition, yPosition] += 1

    return gridLattice, xPosition, yPosition


def createAnimation(gridLattice, xPosition, yPosition, iterations, capture_interval=100,
                    display_interactive=True, coloring='RdGy', is_single_axis_movement=True):
    '''Create animation of brownian motion given initial characteristics.'''

    # Create plot for particle motion.
    fig, ax = plt.subplots()
    ax.set_title("Brownian Motion ({} steps)".format(iterations))

    # Create a list to hold lists of images.
    images = []

    # Iterate for number of desired iterations.
    for iteration in range(iterations):

        # Update grid and positions.
        gridLattice, xPosition, yPosition = updateGrid(xPosition, yPosition,
                                                       gridLattice, is_single_axis_movement)

        # Only generate every 100 frames.
        if iteration % capture_interval == 0:

            # Create image from updated grid and add wrapped in a list.
            image = ax.imshow(gridLattice, animated=True, cmap=coloring)
            images.append([image])

        # Display initial image before animating.
        if iteration == 0:
            ax.imshow(gridLattice, cmap=coloring)

    # Create an animation with generated images.
    brownian_animation = animation.ArtistAnimation(fig, images, interval=100,
                                                   blit=True, repeat_delay=10)
    brownian_animation.save("brownian.gif")

    # Display graph if specified.
    if display_interactive:
        plt.show()


if __name__ == "__main__":

    # Add argument to allow skipping interactive elements from command line.
    parser = argparse.ArgumentParser(description="Create an animation of brownian motion.")
    parser.add_argument('--multiaxismovement', action='store_true', dest='multiaxismovement',
                        help='Limit particle to movement along one axis per step.')
    parser.add_argument('--displayinteractive', action='store_true', dest='displayinteractive',
                        help='Open a window with resultant animation.')

    args = parser.parse_args()
    multiaxismovement = args.multiaxismovement
    displayinteractive = args.displayinteractive

    # Generate grid and determine starting position.
    length = 101
    gridLattice = grid(length, length)
    xPosition, yPosition = initialPosition(gridLattice)

    # Draw point at inital position.
    gridLattice[xPosition, yPosition] = 1

    # Create animation.
    createAnimation(gridLattice, xPosition, yPosition, 10_000, display_interactive=displayinteractive,
                    coloring='RdGy', is_single_axis_movement=(not multiaxismovement))
