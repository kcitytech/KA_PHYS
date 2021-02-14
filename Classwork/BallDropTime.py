#!/usr/bin/env python3
# Example 2.1

print("Example 2.1")

# Prompt user for height and time elapsed for ball falling.
initialHeight = float(input("Height of tower (meters):"))
timeFalling   = float(input("  Time Elapsed (seconds):"))

# Calculate distance traveled by the ball given time specified.
gravitationalConstant = 9.81
distanceTraveled      = .5 * gravitationalConstant * (timeFalling**2)

# Determine if distance traveled exceeds height of tower.
if distanceTraveled >= initialHeight:
    
    # If the distance calculated is higher than the tower, the ball impacted the ground.
    print("The ball is at ground level after falling {} meters (the height of the tower).".format(initialHeight))
else:
    
    # Display the distance of the ball from the ground.
    print("The ball is ~{} meters above the ground.".format(initialHeight-distanceTraveled))