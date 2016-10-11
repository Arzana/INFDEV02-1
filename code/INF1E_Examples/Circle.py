from math import sqrt											# Import the function for square roots from the math file.

def GetIntInput(msg: str):										# Define a function for safely getting integral input from the user.
	result = None												# Define a variable named 'result' for storing the integral value.
	while (result == None):										# Loop until we have a valid input.
		print(msg, end = '')									# Display the message specified and make sure the user can type on the end of that line.
		
		try:													# Define a 'try catch' structure to catch exceptions.
			result = int(input())								# Get the input from the user and try to convert it to a int.
		except:													# If this raises an error do nothing; otherwise result is an int and the loop can end.
			pass
	return result												# Return the integral value received.
	
def GetCircleStr(diameter: int):								# Define a function for creating a circle in string format.
	result = ''													# Define a variable named 'result' for storing the characters calculated.
	r = diameter / 2.0											# Get the radius of the circle and make sure it is stored as a floating point value.

	for y in range(0, diameter + 1):							# Loop through all vertical point in the bounding box of the circle.
		for x in range(0, diameter + 1):						# Loop through all horizontal points in the bounding box of the circle.
			a = y - r											# Get the distance in height from the centre of the circle to the current x coordinate
			b = x - r											# Get the distance in width from the centre of the circle to the current y coordinate.
			c = sqrt(a * a + b * b)								# Get the direct distance from the centre of the circle to the current coordinate. 
			
			if (c <= r):										# If the direct distance from the centre of the circle to the current coordinate is smaller or equal to the radius.
				result += '*'									# Add a '*' to the string if the coordinate lays within the circle.
			else:
				result += ' '									# Add a ' ' to the string if the coordinate lays outside of the circle.
		result += '\n'											# At the end of every vertical iteration add a newline to the string.
				
	return result												# Return the complete result string.

d = GetIntInput("Please enter the diameter of the circle: ")	# Get the diameter of the circle from the user.
print(GetCircleStr(d))											# Print the circle generated to the screen.
input("Press any key to continue...")							# Display an message so the user know what to do next.