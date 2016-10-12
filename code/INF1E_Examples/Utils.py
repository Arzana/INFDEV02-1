def GetIntInput(msg: str):											# Define a function for safely getting integral input from the user.
	result = None													# Define a variable named 'result' for storing the integral value.
	while (result == None):											# Loop until we have a valid input.
		print(msg, end = '')										# Display the message specified and make sure the user can type on the end of that line.
			
		try:														# Define a 'try catch' structure to catch exceptions.
			result = int(input())									# Get the input from the user and try to convert it to a int.
		except:														# If this raises an error do nothing; otherwise result is an int and the loop can end.
			pass	
	return result
	
def Populate(char: chr, amount: int):								# Define a function to replace the 'string * int' operator. 
	if (amount < 0):												# If the specified amount if less than zero throw an exception.
		raise ValueError("Amount must be bigger or equal to zero!")
		
	result = ''														# Define a variable named 'result' for storing the string output.
							
	for i in range(amount):											# Add the specified char to the result for the specified amount.
		result += char
	
	return result