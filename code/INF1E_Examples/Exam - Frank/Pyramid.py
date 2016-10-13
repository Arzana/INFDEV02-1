from Utils import GetIntInput, Populate

def CreatePyramidStr(height: int):
	scalar = 2
	width = height * scalar + 1
	result = ''
	
	x = 1
	for y in range(1, height + 1):
		spaces = width - (x >> 1)
		result += Populate(' ', spaces)
		result += Populate('*', x)
		result += Populate(' ', spaces)
		
		x += scalar
		if (y < height): result += '\n'
		
	return result
	
def Main():
	print("Welcome to the pyramid program.")
	h = GetIntInput("Please enter the height of the pyramid required: ")
	print(CreatePyramidStr(h))
	input("Press any key to continue...")
	
if (__name__ == "__main__"): Main()