from Utils import GetIntInput										# Import the function GetIntInput from the Utils file.
from math import sqrt												# Import the function for square roots from the math file.
		
def GetCircleStr(diameter: int):									# Define a function for creating a circle in string format.
	result = ''														# Define a variable named 'result' for storing the characters calculated.
	r = diameter / 2.0												# Get the radius of the circle and make sure it is stored as a floating point value.
	
	for y in range(0, diameter + 1):								# Loop through all vertical point in the bounding box of the circle.
		for x in range(0, diameter + 1):							# Loop through all horizontal points in the bounding box of the circle.
			a = y - r												# Get the distance in height from the centre of the circle to the current x coordinate
			b = x - r												# Get the distance in width from the centre of the circle to the current y coordinate.
			c = sqrt(a * a + b * b)									# Get the direct distance from the centre of the circle to the current coordinate. 
				
			if (c <= r):											# If the direct distance from the centre of the circle to the current coordinate is smaller or equal to the radius.
				result += '*'										# Add a '*' to the string if the coordinate lays within the circle.
			else:	
				result += ' '										# Add a ' ' to the string if the coordinate lays outside of the circle.
		if (y < diameter): result += '\n'							# At the end of every vertical iteration add a newline to the string, unless it is the last iteration.
					
	return result													# Return the complete result string.

def Main():
	d = GetIntInput("Please enter the diameter of the circle: ")	# Get the diameter of the circle from the user.
	print(GetCircleStr(d))											# Print the circle generated to the screen.
	input("Press any key to continue...")							# Display an message so the user know what to do next.
	
if (__name__ == "__main__"): Main()