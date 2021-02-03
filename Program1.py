# Karim Ahmed
# Exercise 2.1
# Version 1.0.0

# Warning: Command line arguments are not currently validated.

import math
import argparse

def promptHeight():

	# Create variable for height of ball, -1 will denote invalid value.
	height = -1
	
	# Prompt user until valid height is provided.
	while height == -1:
		
		# Prompt user for height and flag invalid string value.
		try:
			height = float(input("Height of ball (meters):"))
		except:
			height = -1
			
		# If height is invalid then prompt user to enter valid number.
		if height < 0:
			height = -1
			print(" Invalid height: Height must be zero or positive real number.")
	
	return height

# Main function
if __name__ == "__main__":

	# Add argument to allow skipping interactive elements from command line.
	parser = argparse.ArgumentParser(description = "Parser")
	parser.add_argument('--height', type=float, help='Height of ball (in meters)')
	args = parser.parse_args()
	
	# Display program info
	print("Exercise 2.1 - Ball Drop")
	
	# Use passed in height if given, otherwise prompt for height.
	height = -1
	
	# Use passed in value if given for height.
	height = args.height
	if args.height is None:
		height = promptHeight()

	# Calculate time for ball to fall the specified distance (assuming no air resistance).
	LOCAL_GRAVITY = 9.81
	timeSeconds    = math.sqrt((2*height)/LOCAL_GRAVITY)
		
	# Display time for ball to hit, rounded to 4 decimal places.
	print("The ball will take approximately {} seconds to hit the ground.".format(round(timeSeconds,4)))