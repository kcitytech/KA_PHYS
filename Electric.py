#!/usr/bin/env python3
# 5.21 Differentiation
# Verify using: https://phet.colorado.edu/sims/html/charges-and-fields/latest/charges-and-fields_en.html
# Recommend using nC instead of C.

import numpy as np
import astropy.constants as constants
import astropy.units as units
import matplotlib.pyplot as plt
import argparse


def electricPotential(pointCharge, distance, maxPotentialVolts=10000):
    '''Calculate electric potential in volts.'''

    # Prevent potentials tending to infinity.
    if distance < .001:
        return maxPotentialVolts * units.V

    else:
        # Find electric potential (Volts = Coulomb/Farad) and cast to volts.
        result = (pointCharge * units.C)/(4 * np.pi * constants.eps0 * (distance * units.meter))
        return result.value * units.V


def electricPotentials(pointCharge, distances):
    '''Calculate electric potentials for multiple distances. Note: Units are removed.'''

    # Calculate voltage at every distance.
    return [electricPotential(pointCharge, distance).value for distance in distances]


def squareGrid(size_in_cm=100):
    '''Create a grid of the specified dimensions and scale.'''

    # Create 2D grid of x/y coordinate for each point.
    sameInterval = np.linspace(-1, 1, num=size_in_cm)
    xs, ys = np.meshgrid(sameInterval, sameInterval)
    return xs, ys


def pythagoreanDistance(x1, y1, x2, y2):
    '''Calculate distances between two points.'''

    # Calculate distance using pythagorean theorem.
    return np.sqrt((x2-x1)**2+(y2-y1)**2)


def pointCharge(x, y, chargeInNanocolombs):
    '''Specify a point charge.'''

    # Convert charge into nanocolombs.
    return {"x": x, "y": y, "charge": chargeInNanocolombs*1e-9}


def gridVoltagesDueToPointCharge(charge, distances):
    '''Calculate voltage at each point on grid resulting from charge.'''

    # Calculate list of voltages, unraveling for simplicity then reshaping to row array.
    voltages = electricPotentials(charge, np.ravel(distances))
    shapedVoltages = np.array(voltages).reshape(distances.shape[0], distances.shape[1])
    return shapedVoltages


def gradientVectorComponents(x, y, charge, xs, ys):
    '''Calculate gradient vector components resulting from to point charge.'''

    # Calculate the distances to the adjacent points.
    distancesLeft = pythagoreanDistance(x, y, xs-0.001, ys)
    distancesRight = pythagoreanDistance(x, y, xs+0.001, ys)
    distancesUp = pythagoreanDistance(x, y, xs, ys+0.001)
    distancesDown = pythagoreanDistance(x, y, xs, ys-0.001)

    # Calculate the corresponding voltages to each point.
    voltagesLeft = gridVoltagesDueToPointCharge(charge, distancesLeft)
    voltagesRight = gridVoltagesDueToPointCharge(charge, distancesRight)
    voltagesUp = gridVoltagesDueToPointCharge(charge, distancesUp)
    voltagesDown = gridVoltagesDueToPointCharge(charge, distancesDown)

    # Calculate x & y components. NOTE: Subtraction MUST be done in increasing order to prevent flipped sign.
    xComponents = voltagesLeft - voltagesRight
    yComponents = voltagesDown - voltagesUp

    return xComponents, yComponents


def voltageColorsForGridVoltages(gridVoltages, useSimpleColoring=True):
    '''Calculate grid voltages for every point in grid.'''

    # Sum voltages due to each point charge to determine total voltages.
    totalVoltages = sum(gridVoltages)

    # When using simple coloring large magnitudes close to point charge will dominate.
    if useSimpleColoring:
        return totalVoltages
    else:

        # Provide color gradient using log preserving sign instead of range.
        # NOTE: Misalignment is due to point not on grid line, use values such as xs[0][-15] for exact alignment (to machine precision).
        # TODO: NOTE: This will currently result in division by zero warning if exact points are used.
        return totalVoltages/abs(totalVoltages) * np.log(abs(totalVoltages))


def plotElectricPotential(xs, ys, voltageColors, pointCharges=None):
    '''Plot electric field.'''

    # Configure general graphing.
    plt.figure('Point Charges')
    plt.title('Electric Potential')
    plt.xlabel('X position (Meters)')
    plt.ylabel('Y position (Meters)')
    plt.axis('square')
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)

    # Plot point charges, create labels and annotations. Note minor asymetries in color are due to positioning off grid.
    plt.pcolormesh(xs, ys, voltageColors, cmap='coolwarm_r', shading='auto')

    # If the point charges are provided plot to create legend.
    if pointCharges is not None:
        plotPointCharges(pointCharges)

    # Show plot.
    plt.show()


def plotPointCharges(pointCharges):
    '''Plot point charges points.'''

    # If point charges are given, plot guide.
    index = 0
    for pointCharge in pointCharges:

        # Plot point charge.
        chargeLabel = "{}) {}C".format(index, pointCharge['charge'])
        plt.scatter(pointCharge['x'], pointCharge['y'], label=chargeLabel, s=2)
        plt.annotate(str(index), (pointCharge['x'], pointCharge['y']))
        index += 1

    # Generate a legend for the plot.
    plt.legend(loc=1)


def plotElectricField(xs, ys, xArrow, yArrow, logMagnitude, pointCharges=None,width=0.002):
    '''Plot electric field due to point charges as grid of arrows with coloring.'''

    # Configure general graphing options.
    plt.figure('Arrow Graph')
    plt.title('Point Charges')
    plt.xlabel('X position (Meters)')
    plt.ylabel('Y position (Meters)')
    plt.axis('square')
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)

    # Plot arrows on quiver plot. Using tight layout will remove top/bottom whitespace padding.
    plt.quiver(xs, ys, xArrow, yArrow, logMagnitude, cmap='hsv',width=0.002)

    # If the point charges are provided plot to create legend.
    if pointCharges is not None:
        plotPointCharges(pointCharges)

    # Show plot.
    plt.show()


def calculateXYComponentsForPointCharges(pointCharges, xs, ys):
    '''Calculate arrow components.'''

    # Sum the x components.
    xComponentsSummed = 0
    yComponentsSummed = 0

    # Iterate point charges to add x and y components.
    for pointCharge in pointCharges:

        # Calculate the vector components for gradient.
        xComponents, yComponents = gradientVectorComponents(pointCharge["x"], pointCharge["y"], pointCharge["charge"], xs, ys)
        xComponentsSummed += xComponents
        yComponentsSummed += yComponents

    return xComponentsSummed, yComponentsSummed


def arrowComponentsForXandYComponents(xComponents, yComponents):
    '''Calculate arrow components from X & Y components.'''

    # Calculate magnitude of components and normalize so arrows are same length.
    magnitude = np.sqrt(xComponents**2 + yComponents**2)
    normalizedXComp = xComponents/magnitude
    normalizedYComp = yComponents/magnitude

    # Compute log of magnitude to better utilize plot coloring without having to deal with range.
    logMagnitude = np.log(magnitude)
    
    # Plot the arrows with scaling to fit on grid.
    scaling = 0.02
    xArrow = scaling*normalizedXComp
    yArrow = scaling*normalizedYComp

    return xArrow, yArrow, logMagnitude

def plotDesiredArrowGraph(xs, ys, xArrow, yArrow, logMagnitude, pointCharges):

    # Create new arrays for graphing with fewer arrows.
    new_xs = []
    new_ys = []
    new_xArrow = []
    new_yArrow = []
    new_logMagnitude = []

    # Specify interval for graphing (indexes to place arrows at).
    interval = np.arange(0,100,5)

    # Iterate indexes to only add specified intervals for rows and columns.
    for index in interval:

        # Add values to the new array.
        new_xs.append(xs[index][interval])
        new_ys.append(ys[index][interval])
        new_xArrow.append(xArrow[index][interval])
        new_yArrow.append(yArrow[index][interval])
        new_logMagnitude.append(logMagnitude[index][interval])

    # Create an electric field with new values.
    plotElectricField(new_xs, new_ys, new_xArrow, new_yArrow, new_logMagnitude, pointCharges)


if __name__ == "__main__":

    print("5.21: Electric field of a charge distribution")

    # Add argument to allow skipping interactive elements from command line.
    parser = argparse.ArgumentParser(description="Display an electric field for two point charges.")
    parser.add_argument('--widecolor', action='store_false', dest='widecolor', help='Whether to fill color.')
    args = parser.parse_args()
    widecolor = args.widecolor

    # Verify electric potential provides reasonable voltages. 1nC at 1meter ~= 9V
    assert(np.ceil(electricPotential(1e-9, 1).value) == 9)

    # Create a grid to place point charges on.
    xs, ys = squareGrid(size_in_cm=100)

    # Create a point charge and calculate distances for every point.
    pointChargeA = pointCharge(-.1, 0, 1*1e9)
    distancesA = pythagoreanDistance(pointChargeA["x"], pointChargeA["y"], xs, ys)
    resultsA = gridVoltagesDueToPointCharge(pointChargeA["charge"], distancesA)

    # Create a point charge and calculate distances for every point.
    pointChargeB = pointCharge(.1, 0, -1*1e9)
    distancesB = pythagoreanDistance(pointChargeB["x"], pointChargeB["y"], xs, ys)
    resultsB = gridVoltagesDueToPointCharge(pointChargeB["charge"], distancesB)

    # Calculate the grid voltages by summing voltages due to individual charges.
    pointCharges = [pointChargeA, pointChargeB]
    gridVoltages = np.array([resultsA, resultsB])
    voltageColors = voltageColorsForGridVoltages(gridVoltages, useSimpleColoring=widecolor)

    # Calculate components.
    xComponents, yComponents = calculateXYComponentsForPointCharges(pointCharges, xs, ys)
    xArrow, yArrow, logMagnitude = arrowComponentsForXandYComponents(xComponents, yComponents)

    # Plot electric potential.
    plotElectricPotential(xs, ys, voltageColors, pointCharges)
    plotElectricField(xs, ys, xArrow, yArrow, logMagnitude, pointCharges)
    
    # Plot using request to include fewer (but larger arrows).
    plotDesiredArrowGraph(xs, ys, xArrow, yArrow, logMagnitude, pointCharges)
