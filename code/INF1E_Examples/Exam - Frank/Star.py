from Utils import GetIntInput, Populate

def CreateStarStr(size: int):
	result = ''
	hafS = size >> 1
	
	x = 0
	for y in range(size):
		dist = abs(hafS - y)
		if (dist == 0):
			result += Populate('*', size)
		else:
			for i in range(3):
				if (not i): 
					result += Populate(' ', x)
				result += '*'
				if (i < 2): result += Populate(' ', dist - 1)
				
		x = x + 1 if y < hafS else x - 1
		if (y + 1 < size): result += '\n'
				
	return result
	
def Main():
	print("Welcome to the star program.")
	s = GetIntInput("Please enter the diameter of the star: ")
	print(CreateStarStr(s))
	input("Press any key to continue...")
	
if (__name__ == "__main__"): Main()