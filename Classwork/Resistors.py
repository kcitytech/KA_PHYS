#!/usr/bin/env python3
# Exercise 6.1
# Verified using https://phet.colorado.edu/en/simulation/circuit-construction-kit-dc

import numpy as np

print("Exercise 6.1 - Resistors Circuit - Junction Voltage Solver\n")

# Create equation for point junctions.
def equationForPoint(point, linkPoints):
    return "+".join(['([{}]-[{}])/R '.format(point, linkPoint) for linkPoint in linkPoints])

# Enable visualization for matrix operations.
def matrixOperationPrint(actionDescription, matrix):
    
    # Print description of matrix operation.
    np.set_printoptions(suppress=True)
    print(actionDescription)
    print(matrix)
    print("____")

# Define connections between points. V+: Refers to top point V-: Lower (https://en.wikipedia.org/wiki/IC_power-supply_pin).
v1Links = ['V+','V2','V3','V4']
v2Links = ['V1','V4','V-']
v3Links = ['V+','V1','V4']
v4Links = ['V1','V2','V3','V-']

# Generate equations for all points and display.
points    = {'V1':v1Links, 'V2':v2Links, 'V3':v3Links, 'V4':v4Links}
equations = {point:equationForPoint(point, points[point]) for point in points}
[print("{} Equation: {}".format(point, equations[point])) for point in equations]

# Manually rewritten equations for resistor values..
v1EquationSimplified = '4[V1]-[V+]-[V2]-[V3]-[V4]=0'
v2EquationSimplified = '3[V2]-[V1]-[V4]-[V-]=0'
v3EquationSimplified = '3[V3]-[V+]-[V1]-[V4]=0'
v4EquationSimplified = '4[V4]-[V1]-[V2]-[V3]-[V-]=0'

# Plug in values V+ = 5 and V- = 0 and order resistors for matrix.
v1EquationOrdered = '+4[V1] -1[V2] -1[V3] -1[V4] = 5'
v2EquationOrdered = '-1[V1] +3[V2] -0[V3] -1[V4] = 0'
v3EquationOrdered = '-1[V1] -0[V2] +3[V3] -1[V4] = 5'
v4EquationOrdered = '-1[V1] -1[V2] -1[V3] +4[V4] = 0'

# Manually convert to float 2D array. [V1 V2 V3 V4 V_Known]. np.maxtrix may be depreciated in the future
matrix = np.array([[ 4, -1, -1, -1, 5],
                    [-1,  3,  0, -1, 0],
                    [-1,  0,  3, -1, 5],
                    [-1, -1, -1,  4, 0]], dtype=float)

print("____\nMatrix:\n{}\n____".format(matrix))

# Manually perform matrix operations and descriptions. Note: Description uses zero-indexing.
# NOTE: This can be accomplished in way fewer steps and could be massively reduced.
matrix[0] *= .25
matrixOperationPrint("Row 0: Divide by 4.", matrix)

matrix[1] += matrix[0]
matrix[2] += matrix[0]
matrix[3] += matrix[0]
matrixOperationPrint("Rows 1, 2 & 3: Add Row 0.", matrix)

matrix[1] /= 2.75
matrixOperationPrint("Row 1: Multiply by 2.75.", matrix)

matrix[0] -= matrix[2]
matrixOperationPrint("Row 0: Subtract Row 2.", matrix)

matrix[2] *= 4
matrix[2] += matrix[1]
matrixOperationPrint("Row 2: Multiply by 4 then add Row 1.", matrix)

matrix[3] /= 1.25
matrix[3] += matrix[1]
matrixOperationPrint("Row 3: Divide by 1.25 then add Row 1.", matrix)

matrix[2] /= matrix[2,2]
matrixOperationPrint("Row 2: Divide by the value of (2nd row, 2nd column).", matrix)

matrix[1] -= matrix[3]
matrixOperationPrint("Row 1: Subtract Row 3.", matrix)

matrix[3] /= matrix[3,2]
matrixOperationPrint("Row 3: Divide by the value of (3rd row, 2nd column).", matrix)

matrix[3] -= matrix[2]
matrixOperationPrint("Row 3: Subtract Row 2.", matrix)

matrix[3] /= matrix[3,3]
matrixOperationPrint("Row 3: Divide by the value of (3rd row, 3rd column).", matrix)

matrix[2] += .5* matrix[3]
matrixOperationPrint("Row 2: Add the value of (.5 times Row 3).", matrix)

matrix[1] -= matrix[2]
matrix[1] += 3*matrix[3]
matrixOperationPrint("Row 1: Subtract Row 1 then add (3 times Row 3).", matrix)

matrix[0] += 3*matrix[2]
matrix[0] -= matrix[3]
matrixOperationPrint("Row 1: Add (3 times Row 2) then subtract Row 3.", matrix)

# Convert to numpy format and solve.
coefficients = matrix[:,0:4]
dependents   = matrix[:,4]
rref         = np.ravel(matrix[:,4])
voltages     = np.ravel(np.linalg.solve(coefficients, dependents))
actual       = [3, 5/3, 10/3, 2]

# Compare results to actual results using phet.
print("        Manual RREF : {}".format(rref))
print("Numpy linalg.solve(): {}".format(voltages))
print("           Reference: {}".format(actual))