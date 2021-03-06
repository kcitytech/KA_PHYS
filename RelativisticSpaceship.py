#!/usr/bin/env python3
# Exercise 2.4
# Useful resource: WSU: Space, Time, and Einstein with Brian Greene - https://www.youtube.com/watch?v=CKJuC5CUMgU

import math
import argparse

# Prompt the user interactively for the distance traveled by the spaceship.
def promptDistance():
	
	# Prompt user until valid distance is provided. -1 denotes invalid value.
	distance = -1
	while distance == -1:
		
		# Prompt user for height and flag invalid string value.
		try:
			distance = float(input("Distance (light years):"))
		except:
			distance = -1
			
		# Prompt user to enter valid distance until provided.
		if not isValidDistance(distance):
			distance = -1
			print(" Invalid distance: Distance must be zero or positive real number.")
			
	return distance

# Proft the user interactively for the speed of the spaceship.
def promptSpeed():
	
	# Prompt user until valid speed is provided. -1 denotes invalid value.
	speed = -1
	while speed == -1:
		
		# Prompt user for height and flag invalid string value.
		try:
			speed = float(input("Speed (Decimal fraction speed of light):"))
		except:
			speed = -1
			
		# Prompt user to enter valid speed until provided.
		if not isValidSpeed(speed):
			speed = -1
			print(" Invalid speed: Speed must be between zero and one, exclusive.")
	
	return speed

# Validate distance.
def isValidDistance(distance):
	
	# Ensure height (float) is positive (or zero).
	return distance >= 0

# Validate speed.
def isValidSpeed(speed):
	
	# Ensure speed (float) is between 0 and 1.
	return speed >= 0 and speed <= 1

# Access command line argument distance.
def argumentDistance(distance):
	
	# If no distance is provided, interactively prompt.
	if args.distance is None:
		distance = promptDistance()
	
	# If distance argument is valid use provided value.
	elif isValidDistance(args.distance):
		distance = args.distance
		
	# When used non-interactively exit if flag argument is invalid.
	else:
		raise ValueError(' Invalid distance: Distance must be zero or positive real number.')
	
	return distance

# Access command line argument speed.
def argumentSpeed(speed):
	
	# If no speed is provided, interactively prompt.
	if args.speed is None:
		speed = promptSpeed()
		
	# If speed argument is valid use provided value.
	elif isValidSpeed(args.speed):
		speed = args.speed
	
	# When used non-interactively exit if flag argument is invalid.
	else:
		raise ValueError(' Invalid speed: Speed must be between zero and one, exclusive.')
	
	return speed
	
# Calculate earth observer time for distance and speed.
def earthObserverTime(distance, speed):
	return distance/speed
		
# Calculate spaceship observer time for distance and speed.
def spaceshipObserverTime(distance, speed):
	
	# Calculate lorentz factor.
	lorentzFactor = 1/math.sqrt(1-((speed**2)))
	
	# Use lorentz factor to determine how the observer on the spacecraft will percieve travel time.
	spaceshipObserverTimeYears = earthObserverTimeYears/lorentzFactor
	
	return spaceshipObserverTimeYears
	
# Main function
if __name__ == "__main__":
	
	# Add argument to allow skipping interactive elements from command line.
	parser = argparse.ArgumentParser(description = "Calculate time experienced by observers for relativistic speeds.")
	parser.add_argument('--distance', type=float, help='Distance (in lightyears)')
	parser.add_argument('--speed'   , type=float, help='Speed of spacecraft (in c)')
	args = parser.parse_args()

	# Display program info.
	print("Exercise 2.4 - Spaceship")
	
	# Determine distance and speed to use for calculation.
	distance                   = argumentDistance(args.distance)
	speed                      = argumentSpeed(args.speed)
	earthObserverTimeYears     = earthObserverTime(distance, speed)
	spaceshipObserverTimeYears = spaceshipObserverTime(distance, speed)
		
	# Display time experienced by observers.
	print("The observer on earth expects the spaceship to reach its target in ~{} years.".format(round(earthObserverTimeYears,4)))
	print("The observer on the spaceship perceives ~{} years elapsing before reaching the planet.".format(round(spaceshipObserverTimeYears,4)))