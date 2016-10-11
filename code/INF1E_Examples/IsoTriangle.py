from Utils import GetIntInput, Populate											# Import the functions GetIntInput and Populate from the Utils file.

def GetIsoTriangleStr(height: int):												# Define a function for creating a triangle in string format.
	scalar = 2																	# Define a variable for the the amount of '*' added per vertical iteration.
	width = (height - 1) * scalar + 1											# Get the absolute width of the final triangle.
	result = ''																	# Define a variable named 'result' for storing the characters calculated.
	
	x = 1																		# Define the amount of '*' characters used in the current iteration.
	for y in range(1, height + 1):												# Loop through the height specified (starts at 1 for ease of use later).
		spaces = (width - x) >> 1												# Get the amount of spaces needed at both ends of the triangle ('>> 1' does the same as '/ 2', its just faster).
		result += Populate(' ', spaces)											# Add the right sided spaces to the result string. 
		result += Populate('*', x)												# Add the '*' characters to the result string.
		result += Populate(' ', spaces)											# Add the left sided spaces to the result string.
		
		if (y < height):
			result += '\n'														# At the end of every vertical iteration add a newline to the string, unless it is the last iteration.
			x += scalar															# Add the scalar to the horizontal specifier. 
		
	return result;																# Return the complete result string.
	
def Main():
	h = GetIntInput("Please specify the height of the isosceles triangle: ")	# Get the height of the triangle from the user.
	print(GetIsoTriangleStr(h))													# Print the triangle generated to the screen.
	input("Press any key to continue...")										# Display an message so the user know what to do next.
	
if (__name__ == "__main__"): Main()