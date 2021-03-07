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
    return x, y, (chargeInNanocolombs*1e-9)

# Calculate voltage at each point on grid resulting from charge.
def gridVoltagesDueToPointCharge(charge, distances):
    
    # Calculate list of voltages, unraveling for simplicity.
    voltages = electricPotentials(charge, np.ravel(distances))
    
    # Reshape back into row array.
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

# Create a grid to place point charges on.
xs, ys = square100cmGrid()
    
# Create a point charge and calculate distances for every point.
x0, y0, charge0 = pointCharge(-.1, 0, 1*1e-9)
distances0      = pythagoreanDistance(x0, y0, xs, ys)
results0        = gridVoltagesDueToPointCharge(charge0, distances0)

# Create second point charge.
x1, y1, charge1 = pointCharge(.1, 0, -1*1e-9)
distances1      = pythagoreanDistance(x1, y1, xs, ys)
results1        = gridVoltagesDueToPointCharge(charge1, distances1)

# Display volts using log (which requires steps to preserve sign) to use color space without needing to calculate range. 
# Use grid coordinate instead to fix, ex: xs[0][-15] for x to get exact copy (to machine precision).
# However this can result in division by zero since symmetric results will cancel out.
voltageColors = (results0+results1)/abs(results0+results1) * np.log(abs(results0 + results1))
voltageColors = results0+results1

# Plot point charges, create labels and annotations. Note minor asymetries in color are due to positioning off grid.
plt.figure('Graph')
plt.title('Charges')
plt.axis('square')
plt.xlim(-1,1)
plt.ylim(-1,1)
plt.xlabel('X position (Meters)')
plt.ylabel('Y position (Meters)')
plt.pcolormesh(xs, ys, voltageColors, cmap='coolwarm_r', shading = 'auto')
plt.scatter(x0, y0,c='red' ,label='1) +1C',s=3)
plt.scatter(x1, y1,c='cyan',label='2) -1C',s=3)
plt.annotate('¹',(x0,y0))
plt.annotate('²',(x1,y1))
plt.legend()
plt.show()

# Calculate the vector components for gradient.
xComponents0, yComponents0 = gradientVectorComponents(x0, y0, charge0, xs, ys)
xComponents1, yComponents1 = gradientVectorComponents(x1, y1, charge1, xs, ys)

# Sum components of vectors.
xComponentsSummed = xComponents0 + xComponents1
yComponentsSummed = yComponents0 + yComponents1

# Calculate magnitude of components and normalize so arrows are same length.
magnitude       = np.sqrt(xComponentsSummed**2 + yComponentsSummed**2)
normalizedXComp = xComponentsSummed/magnitude
normalizedYComp = yComponentsSummed/magnitude

# Compute log of magnitude to better utilize plot coloring without having to deal with range.
logMagnitude = np.log(magnitude)

# Plot the arrows with scaling to fit on grid.
scaling = 0.02
xArrow  = (scaling*normalizedXComp)
yArrow  = (scaling*normalizedYComp)

# Plot arrows on quiver plot.
plt.figure('Arrow Graph')
plt.title('Point Charges')
plt.xlabel('X position (Meters)')
plt.ylabel('Y position (Meters)')
plt.axis('equal')
plt.quiver(xs, ys, xArrow, yArrow, logMagnitude,cmap='hsv')
plt.scatter(x0,y0,c='red' ,label='1) +1C',s=3)
plt.scatter(x1,y1,c='cyan',label='2) -1C',s=3)
plt.annotate('¹',(x0,y0))
plt.annotate('²',(x1,y1))
plt.legend()
plt.show()

# Define base unit which provides reasonable voltages. 1nC at 1meter ~= 9V
nanocoulomb = 1e-9
assert(np.ceil(electricPotential(nanocoulomb, 1).value) == 9)