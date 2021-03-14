#!/usr/bin/env python3
# 5.21 Differentiation
# Verify using: https://phet.colorado.edu/sims/html/charges-and-fields/latest/charges-and-fields_en.html
# Recommend using nC instead of C.

import numpy             as np
import astropy.constants as constants
import astropy.units     as units
import matplotlib.pyplot as plt

# Calculate electric potential in volts.
def electricPotential(pointCharge, distance, maxPotentialVolts=10000):
    
    # Prevent potentials tending to infinity.
    if distance < .001:
        return maxPotentialVolts * units.V
    
    else:
        # Find electric potential (Volts = Coulomb/Farad) and cast to volts.
        result = (pointCharge * units.C)/(4 * np.pi * constants.eps0 * (distance * units.meter))
        return result.value * units.V

# Calculate electric potentials for multiple distances. Note: Units are removed.
def electricPotentials(pointCharge, distances):

    # Calculate voltage at every distance.
    return [electricPotential(pointCharge, distance).value for distance in distances]

# Create a grid of the specified dimensions and scale.
def square100cmGrid():

    # Create 2D grid of x/y coordinate for each point.
    sameInterval = np.linspace(-1, 1, num=100)
    xs, ys       = np.meshgrid(sameInterval, sameInterval)
    return xs, ys

# Calculate distances between two points.
def pythagoreanDistance(x1, y1, x2, y2):
    
    # Calculate distance using pythagorean theorem.
    return np.sqrt( (x2-x1)**2 + (y2-y1)**2 )

# Specify a point charge.
def pointCharge(x, y, chargeInNanocolombs):
    
    # Convert charge into nanocolombs.
    return {"x":x, "y":y, "charge":chargeInNanocolombs*1e-9}

# Calculate voltage at each point on grid resulting from charge.
def gridVoltagesDueToPointCharge(charge, distances):
    
    # Calculate list of voltages, unraveling for simplicity then reshaping to row array.
    voltages       = electricPotentials(charge, np.ravel(distances))
    shapedVoltages = np.array(voltages).reshape(100,100)
    return shapedVoltages

# Calculate gradient vector components resulting from to point charge.
def gradientVectorComponents(x, y, charge, xs, ys):
    
    # Calculate the distances to the adjacent points.
    distancesLeft  = pythagoreanDistance(x, y, xs-0.001, ys)
    distancesRight = pythagoreanDistance(x, y, xs+0.001, ys)
    distancesUp    = pythagoreanDistance(x, y, xs,       ys+0.001)
    distancesDown  = pythagoreanDistance(x, y, xs,       ys-0.001)
    
    # Calculate the corresponding voltages to each point.
    voltagesLeft   = gridVoltagesDueToPointCharge(charge, distancesLeft)
    voltagesRight  = gridVoltagesDueToPointCharge(charge, distancesRight)
    voltagesUp     = gridVoltagesDueToPointCharge(charge, distancesUp)
    voltagesDown   = gridVoltagesDueToPointCharge(charge, distancesDown)
    
    # Calculate x & y components. NOTE: Subtraction MUST be done in increasing order otherwise sign will be flipped.
    xComponents    = voltagesLeft - voltagesRight
    yComponents    = voltagesDown - voltagesUp
    
    return xComponents, yComponents

# Calculate grid voltages for every point in grid .
def voltageColorsForGridVoltages(gridVoltages, useSimpleColoring=True):
    
    # Sum voltages due to each point charge to determine total voltages.
    totalVoltages = sum(gridVoltages)

    # When using simple coloring large magnitudes close to point charge will dominate.
    if useSimpleColoring:
        return totalVoltages
    else:
        
        # Provide color gradient using log preserving sign instead of range.
        # NOTE: Misalignment is due to point not on grid line, use values such as xs[0][-15] for exact alignment (to machine precision).
        # NOTE: This will currently result in division by zero warning if exact points are used.
        return totalVoltages/abs(totalVoltages) * np.log(abs(totalVoltages))
    
# Plot electric field.
def plotElectricPotential(xs, ys, voltageColors):
        
    # Configure general graphing.
    plt.figure('Point Charges')
    plt.title('Electric Potential')
    plt.xlabel('X position (Meters)')
    plt.ylabel('Y position (Meters)')
    plt.axis('square')
    plt.xlim(-1,1)
    plt.ylim(-1,1)
    
    # Plot point charges, create labels and annotations. Note minor asymetries in color are due to positioning off grid.
    plt.pcolormesh(xs, ys, voltageColors, cmap='coolwarm_r', shading = 'auto')
#    plt.scatter(x0, y0,c='red' ,label='1) +1C',s=3)
#    plt.scatter(x1, y1,c='cyan',label='2) -1C',s=3)
#    plt.annotate('¹',(x0,y0))
#    plt.annotate('²',(x1,y1))
#    plt.legend()
    plt.show()
    
# Plot electric field due to point charges as grid of arrows with coloring.
def plotElectricField(xs, ys, xArrow, yArrow, logMagnitude):
    
    # Configure general graphing options.
    plt.figure('Arrow Graph')
    plt.title('Point Charges')
    plt.xlabel('X position (Meters)')
    plt.ylabel('Y position (Meters)')
    plt.axis('square')
    plt.xlim(-1,1)
    plt.ylim(-1,1)
    
    # Plot arrows on quiver plot. Using tight layout will remove top/bottom whitespace padding.
    plt.quiver(xs, ys, xArrow, yArrow, logMagnitude,cmap='hsv')
#    plt.scatter(x0,y0,c='red' ,label='1) +1C',s=3)
#    plt.scatter(x1,y1,c='cyan',label='2) -1C',s=3)
#    plt.annotate('¹',(x0,y0))
#    plt.annotate('²',(x1,y1))
#    plt.legend(loc=1)
    plt.show()
    
# Calculate arrow components.
def calculateXYComponentsForPointCharges(pointCharges, xs, ys):
    
    # Sum the x components.
    xComponentsSummed = 0
    yComponentsSummed = 0
    
    # Iterate point charges to add x and y components.
    for pointCharge in pointCharges:
        
        # Calculate the vector components for gradient.
        xComponents, yComponents = gradientVectorComponents(pointCharge["x"], pointCharge["y"], pointCharge["charge"], xs, ys)
        xComponentsSummed       += xComponents
        yComponentsSummed       += yComponents
        
    return xComponentsSummed, yComponentsSummed

# Calculate arrow components from X & Y components.
def arrowComponentsForXandYComponents(xComponents, yComponents):
    
    # Calculate magnitude of components and normalize so arrows are same length.
    magnitude       = np.sqrt(xComponents**2 + yComponents**2)
    normalizedXComp = xComponents/magnitude
    normalizedYComp = yComponents/magnitude
    
    # Compute log of magnitude to better utilize plot coloring without having to deal with range.
    logMagnitude = np.log(magnitude)
    
    # Plot the arrows with scaling to fit on grid.
    scaling = 0.02
    xArrow  = scaling*normalizedXComp
    yArrow  = scaling*normalizedYComp
    
    return xArrow, yArrow, logMagnitude
    
# Main
if __name__ == "__main__":

    print("5.21: Electric field of a charge distribution")

    # Verify electric potential provides reasonable voltages. 1nC at 1meter ~= 9V
    assert(np.ceil(electricPotential(1e-9, 1).value) == 9)

    # Create a grid to place point charges on.
    xs, ys = square100cmGrid()
    
    # Create a point charge and calculate distances for every point.
    pointChargeA = pointCharge(-.1, 0, 1*1e9)
    distancesA   = pythagoreanDistance(pointChargeA["x"], pointChargeA["y"], xs, ys)
    resultsA     = gridVoltagesDueToPointCharge(pointChargeA["charge"], distancesA)

    # Create a point charge and calculate distances for every point.
    pointChargeB = pointCharge(.1, 0, -1*1e9)
    distancesB   = pythagoreanDistance(pointChargeB["x"], pointChargeB["y"], xs, ys)
    resultsB     = gridVoltagesDueToPointCharge(pointChargeB["charge"], distancesB)

    # Calculate the grid voltages by summing voltages due to individual charges.
    pointCharges  = [pointChargeA, pointChargeB]
    gridVoltages  = np.array([resultsA, resultsB])
    voltageColors = voltageColorsForGridVoltages(gridVoltages,useSimpleColoring=True)
    
    # Calculate 
    xComponents, yComponents     = calculateXYComponentsForPointCharges(pointCharges, xs, ys)
    xArrow, yArrow, logMagnitude = arrowComponentsForXandYComponents(xComponents, yComponents)
    
    # Generate plots
    plotElectricPotential(xs, ys, voltageColors)
    plotElectricField(xs, ys, xArrow, yArrow, logMagnitude)