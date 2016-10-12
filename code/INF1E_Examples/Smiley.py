from Utils import GetIntInput											# Import the function GetIntInput from the Utils file.
from math import sqrt													# Import the function for square roots from the math file.

def Clamp(mi, ma, v):													# Define a function for clamping values between a specified minimum and a maximum.
	return max(mi, min(ma, v))											# Example: (0, 10, 14) => max(0, min(10, 14)) => max(0, 10) => 10.

def CreateSmileyStr(radius: int):										# Define a function for creating a smiley in string format.
	d = radius << 1														# Get the diameter of the circle ('<< 1' is a faster was of writing '* 2').
	hafR = radius >> 1													# Get half of the radius ('>> 1' is a faster was of writing '/ 2').
	sesqui = radius + hafR												# Get one and a half of the radius.
	
	result = ''															# Define a variable named 'result' for storing the characters calculated.
	for y in range(d + 1):												# Loop through all vertical point in the bounding box of the circle.
		for x in range(d + 1):											# Loop through all horizontal points in the bounding box of the circle.
			char = ' '													# Define a variable named 'char' for storing the character that needs to be added to the result (space as default).
			a = y - radius												# Get the distance in height from the centre of the circle to the current x coordinate.
			b = x - radius												# Get the distance in width from the centre of the circle to the current y coordinate.
			c = round(sqrt(a * a + b * b))								# Get the direct distance from the centre of the circle to the current coordinate and round it to a whole number.
			
			if (c == radius): 											# If the direct distance to the current coordinate is equal to the radius, set char to '*' (face shape).
				char = '*'
			elif (x == hafR or x == sesqui):							# If the horizontal component is equal to the half radius or to one and a half radius.
				if (y == hafR - 1): 									# If the vertical component is equal to the half radius minus 1, set char to '_' (eyebrow).
					char = '_'
				elif (y == hafR):										# If the vertical component is equal to the half radius, set char to '0' (eyes).
					char = '0'
			elif (y == sesqui and x > hafR and x < sesqui):				# If the vertical component is equal to one and a half radius and the horizontal component is between the half radius and one and a half radius,
				char = '-'												# set char to '-' (mouth).
			elif (y == radius and x == radius):							# If the current coordinate is the centre of the circle, set char to '#' (nose).
				char = '#'
				
			result += char												# Add the calculated character to the result string.
			
		if (y < d): 
			result += '\n'												# At the end of every vertical iteration add a newline to the string, unless it is the last iteration.										
		
	return result														# Return the complete result string.
	
def Main():
	minR = 6															# Define a constant variable to store the minimum radius required from the user.
	maxR = 20															# Define a constant variable to store the maximum radius required from the user.
	
	r = GetIntInput("Please enter the radius of the smiley's face (input will be clamped between (%d - %d): " % (minR, maxR))
	r = Clamp(minR, maxR, r)											# Clamp the user specified radius between the constant minimum and maximum.
	print(CreateSmileyStr(r))											# Print the smiley generated to the screen.
	input("Press any key to continue...")								# Display an message so the user know what to do next.
	
if (__name__ == "__main__"): Main()