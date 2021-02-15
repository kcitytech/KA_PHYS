#!/usr/bin/env python3
# Exercise 2.1: Another ball dropped from a tower

import math
import argparse

def promptHeight():

	# Store height of ball. -1 denotes invalid value.
	height = -1
	
	# Prompt user until valid height is provided.
	while height == -1:
		
		# Prompt user for height and flag invalid input.
		try:
			height = float(input("Height of ball (meters):"))
		except:
			height = -1
			
		# If height is invalid then prompt user to enter valid number.
		if height < 0:
			height = -1
			print(" Invalid height: Height must be zero or positive real number.")
	
	return height

def isValidArgumentHeight(height):
	
	# Ensure height (input as float) is positive (or zero).
	return height >= 0

if __name__ == "__main__":

	# Add argument to allow skipping interactive elements from command line.
	parser = argparse.ArgumentParser(description = "Calculate time for ball to fall specified height.")
	parser.add_argument('--height', type=float, help='Height of ball (in meters)')
	args = parser.parse_args()
	
	# Display program info.
	print("Exercise 2.1 - Ball Drop")
	
	# Store height of ball. -1 denotes invalid value.
	height = -1
		
	# If program is called interactively prompt for height.
	if args.height is None:
		height = promptHeight()
		
	elif isValidArgumentHeight(args.height):
		
		# Use passed in float for height.
		height = args.height
		
	else:
		# When used non-interactively exit if flag argument is invalid.
		raise ValueError('Height must be positive integer/decimal value.')
		
	# Calculate time for ball to fall the specified distance (assuming no air resistance).
	LOCAL_GRAVITY = 9.81
	timeSeconds   = math.sqrt((2*height)/LOCAL_GRAVITY)
		
	# Display time for ball to hit, rounded to 4 decimal places.
	print("The ball will take approximately {} seconds to hit the ground.".format(round(timeSeconds,4)))