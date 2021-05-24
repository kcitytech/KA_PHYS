#!/usr/bin/env python3

import numpy as np

def inefficient_random_walk(free_particles_mask, occupancy_mask, x_points, y_points):
    
    # Reshape free particles mask to make earier to randomly generate values.
    free_particles_mask_rows = np.reshape(np.copy(free_particles_mask), (x_points, y_points))

    # Create a secondary occupancy mask for determining where particles can move.
    occupancy_mask_rows = np.reshape(np.copy(occupancy_mask), (x_points, y_points))

    # Determine new particles mask.
    free_particles_mask_new_rows = np.zeros((x_points, y_points))

    # Iterate each row in the particles mask rows to relocate.
    for row_index in range(y_points):

        # Iterate each particle in the row.
        for column_index in range(x_points):

            # If the position is denoted by 1 then this represents a particle.
            is_particle = (free_particles_mask_rows[row_index, column_index] == 1)
            
            # If particle then calculate new position.
            if is_particle:
                
                # Determine the new position.
                new_position = particle_movement(row_index, column_index, occupancy_mask_rows, x_points, y_points)
                new_row      = new_position[0]
                new_column   = new_position[1]
                free_particles_mask_new_rows[new_row, new_column] = 1
                occupancy_mask_rows[new_row, new_column] = 1
    
    # Reshape arrays and return
    free_particles_mask_reshaped = np.reshape(free_particles_mask_new_rows, x_points*y_points)
    
    return free_particles_mask_reshaped

# Determine the new random movement for a particle.
def particle_movement(row, column, occupied_mask_rows, x_points, y_points):
    
    # Determine position with respect to bounds.
    position = particle_position(row, column, x_points, y_points)
    
    # Determine allowed positions based on extent and neighbors.
    options = []
    
    # If particle is not on the left border add (unless occupied).
    if not position[0]:
        value = option(row, column-1, occupied_mask_rows)
        if value:
            options.append(value)
        
    # If particle is not on the right border add (unless occupied).
    if not position[1]:
        value = option(row, column+1, occupied_mask_rows)
        if value:
            options.append(value)

    # If particle is not on the top border add (unless occupied).
    if not position[2]:
        value = option(row-1, column, occupied_mask_rows)
        if value:
            options.append(value)

    # If particle is not on the bottom border add (unless occupied).
    if not position[3]:
        value = option(row+1, column, occupied_mask_rows)
        if value:
            options.append(value)

    # Randomly chose one of the directional options.
    if len(options) == 0:
        return [row, column] # Return original.
    else:
        # Use workaround with index to allow numpy to select.
        choice_index = np.random.choice(len(options), 1)[0]
        new_position = options[choice_index]
        return new_position
        
def particle_position(row, column, x_points, y_points):
    
    # Determine if particle is on exterior of bounds.
    is_leftmost = (column == 0)
    is_rightmost = (column == x_points-1)
    is_topmost = (row == 0)
    is_bottommost = (row == y_points-1)
    
    return [is_leftmost, is_rightmost, is_topmost, is_bottommost]

def option(row, column, occupied_mask_rows):
    # Determine if occupied.
    position = occupied_mask_rows[row, column]
    is_occupied = (position == 1)
    if not is_occupied:
        return [row, column]

if __name__ == "__main__":

    # frame size
    x_points = 200
    y_points = 200

    # Create free particles mask
    free_particles_mask = np.zeros(x_points*y_points)
    free_particles_mask[10] = 1
    free_particles_mask[15] = 1
    free_particles_mask[9000:9240] = 1

    # Create occupancy mask.
    occupancy_mask = np.zeros(x_points*y_points)
    occupancy_mask[2] = 1
    occupancy_mask[8880:8999] = 1
    occupancy_mask[23] = 1

    import matplotlib.pyplot as plt

    plt.imshow(np.reshape(free_particles_mask,(x_points,y_points)))
    plt.show()
    
    for i in range(400):

        # Perform random walk
        free_particles_mask = inefficient_random_walk(free_particles_mask, occupancy_mask, x_points, y_points)

        mask_free = np.reshape(free_particles_mask, (x_points, y_points))
        mask_locked = np.reshape(occupancy_mask, (x_points, y_points))
        # print(np.sum(occupancy_mask))

        plt.imshow(mask_free+mask_locked)
        plt.savefig('a\{}.png'.format(i))
        # plt.show()