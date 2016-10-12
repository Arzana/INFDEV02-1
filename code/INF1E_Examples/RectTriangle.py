from Utils import GetIntInput, Populate											# Import the functions GetIntInput and Populate from the Utils file.

def GetRectTrglStr(size: int):													# Define a function for creating a triangle in string format.
	result = ''																	# Define a variable named 'result' for storing the characters calculated.
	
	for y in range(1, size + 1):												# Loop through the height specified (starts at 1 for ease of use later).
		result += Populate('*', y)												# Add the needed amount of '*' characters to the result (because the triangle is rectangular this is the same value as the current y coordinate.
		if (y < size): 
			result += '\n'														# At the end of every vertical iteration add a newline to the string, unless it is the last iteration.
	
	return result																# Return the complete result string.
	
def Main():
	s = GetIntInput("Please specify the size of the rectangular triangle: ")	# Get the size of the triangle from the user.
	print(GetRectTrglStr(s))													# Print the triangle generated to the screen.
	input("Press any key to continue...")										# Display an message so the user know what to do next.
	
if (__name__ == "__main__"): Main()