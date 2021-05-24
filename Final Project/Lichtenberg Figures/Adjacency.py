#!/usr/bin/env python3

import numpy as np

def row_mask(row, x_points):
    
    # Create a new mask for the row by shifting left and right using a spacer element.
    left     = row[1:x_points]
    right    = row[0:x_points-1]
    spacer   = np.array([0])

    # Create row mask by merging the shifted rows.
    shifted_left  = np.concatenate((left, spacer) , axis=None)
    shifted_right = np.concatenate((spacer, right), axis=None)
    new_row_mask  = row + shifted_left + shifted_right

    # Since operating like a binary mask change all values greater than 1 to 1.
    new_row_mask[new_row_mask > 1] = 1

    return new_row_mask

def create_adjacency_mask(x_points, y_points, occupancy_mask_by_rows, is_diagnonal_adjacent=False):

    # Create an adjacency mask as series of rows for convenience.
    adjacency_mask_by_rows = np.zeros((x_points, y_points), dtype=int)

    # Iterate each row in the occupancy mask to update adjacency mask.
    for row_index in range(y_points):

        # Access the corresponding row and create a row mask.
        row = occupancy_mask_by_rows[row_index]
        new_row_mask = row_mask(row, x_points)

        # Update the row by adding values.
        adjacency_mask_by_rows[row_index] = adjacency_mask_by_rows[row_index] + new_row_mask

        # Results may be better if diagonal rows are not treated as adjacent.
        row_addition = row
        if is_diagnonal_adjacent:
            row_addition = new_row_mask

        # Add adjacent elements on preceding and subsequent row (excluding first/last rows). This will also mark diagonals which are desired.
        if row_index != 0:
            adjacency_mask_by_rows[row_index-1] = adjacency_mask_by_rows[row_index-1] + row_addition
        if row_index != y_points-1:
            adjacency_mask_by_rows[row_index+1] = adjacency_mask_by_rows[row_index+1] + row_addition

    # Since operating like a binary mask change all values greater than 1 to 1.
    adjacency_mask_by_rows[adjacency_mask_by_rows > 1] = 1

    # return reshaped array.
    return np.reshape(adjacency_mask_by_rows, x_points*y_points)

if __name__ == "__main__":
    '''Perform basic unit tests.'''

    # Create some sample rows for testing.
    row_a = np.array([0,1,0])
    row_b = np.array([0,1,0,1,0])
    row_c = np.array([0,0,0,1,1,0,0,0])
    row_d = np.array([1,0,0])

    # Generate masks.
    mask_a = row_mask(row_a, len(row_a))
    mask_b = row_mask(row_b, len(row_b))
    mask_c = row_mask(row_c, len(row_c))
    mask_d = row_mask(row_d, len(row_d))

    # Validate matches expected.
    assert(np.array_equal(mask_a, np.array([1,1,1])))
    assert(np.array_equal(mask_b, np.array([1,1,1,1,1])))
    assert(np.array_equal(mask_c, np.array([0,0,1,1,1,1,0,0])))
    assert(np.array_equal(mask_d, np.array([1,1,0])))

    # Create basic array to test.
    x_points_a  = 3
    y_points_a  = 3
    test_a      = np.zeros((x_points_a, y_points_a))
    test_a[1,1] = 1

    # Create an adjacency mask.
    adjacency_mask_a = create_adjacency_mask(x_points_a, y_points_a, test_a,is_diagnonal_adjacent=True)
    adjacency_mask_b = create_adjacency_mask(x_points_a, y_points_a, test_a,is_diagnonal_adjacent=False)

    # Verify matches expected
    assert(np.array_equal(np.ones(9), adjacency_mask_a))
    assert(np.array_equal(np.array([0,1,0,1,1,1,0,1,0]), adjacency_mask_b))
    print("OK")