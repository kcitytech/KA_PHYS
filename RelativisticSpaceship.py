#!/usr/bin/env python3
# Exercise 2.4
# Useful resource: WSU: Space, Time, and Einstein with Brian Greene - https://www.youtube.com/watch?v=CKJuC5CUMgU

import math
import argparse

def promptDistance():
	
	# Store distance. -1 will denote invalid value.
	distance = -1
	
	# Prompt user until valid distance is provided.
	while distance == -1:
		
		# Prompt user for height and flag invalid string value.
		try:
			distance = float(input("Distance (light years):"))
		except:
			distance = -1
			
		# If height is invalid then prompt user to enter valid number.
		if distance < 0:
			distance = -1
			print(" Invalid distance: Distance must be zero or positive real number.")
			
	return distance

def promptSpeed():
	
	# Store speed. -1 will denote invalid value.
	speed = -1
	
	# Prompt user until valid distance is provided.
	while speed == -1:
		
		# Prompt user for height and flag invalid string value.
		try:
			speed = float(input("Speed (Decimal fraction speed of light):"))
		except:
			speed = -1
			
		# If height is invalid then prompt user to enter valid number.
		if speed <= 0 or speed >= 1:
			speed = -1
			print(" Invalid speed: Speed must be between zero and one, exclusive.")
	
	return speed

def isValidArgumentDistance(distance):
	
	# Ensure height (input as float) is positive (or zero).
	return distance >= 0

def isValidArgumentSpeed(speed):
	
	# Ensure height (input as float) is positive (or zero).
	return speed >= 0 and speed <= 1

# Main function
if __name__ == "__main__":
	
	# Add argument to allow skipping interactive elements from command line.
	parser = argparse.ArgumentParser(description = "Parser")
	parser.add_argument('--distance', type=float, help='Distance (in lightyears)')
	parser.add_argument('--speed'   , type=float, help='Speed of spacecraft (in c)')
	args = parser.parse_args()

	# Display program info.
	print("Exercise 2.4 - Spaceship")
	
	# Use passed in value if given for distance.
	distance = args.distance
	if args.distance is None:
		distance = promptDistance()
		
	elif isValidArgumentDistance(args.distance):
		
		# Use passed in float for distance.
		distance = args.distance
	
	else:
		# When used non-interactively exit if flag argument is invalid.
		raise ValueError('Invalid distance: Distance must be zero or positive real number.')

	# Use passed in value if given for speed.
	speed = args.speed
	if args.speed is None:
		speed = promptSpeed()
		
	elif isValidArgumentSpeed(args.speed):
			
			# Use passed in float for distance.
			speed = args.speed
			
	else:
		# When used non-interactively exit if flag argument is invalid.
		raise ValueError(' Invalid speed: Speed must be between zero and one, exclusive.')
					
	# Calculate perceived travel time from earth observer.
	earthObserverTimeYears = distance/speed
	
	# Calculate lorentz factor .
	lorentzFactor = 1/math.sqrt(1-((speed**2)))
	
	# Use lorentz factor to determine how the observer on the spacecraft will percieve 	travel time.
	spaceshipObserverTimeYears = earthObserverTimeYears/lorentzFactor
	
	# Display time experienced by observers.
	print("The observer on earth expects the spaceship to reach its target in ~{} years.".format(round(earthObserverTimeYears,4)))
	print("The observer on the spaceship perceives ~{} years elapsing before reaching the planet.".format(round(spaceshipObserverTimeYears,4)))