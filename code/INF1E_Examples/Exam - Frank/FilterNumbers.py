from Utils import GetIntInput

def CreateDivisibleStr(n: int):
	result = ''
	
	for i in range(2, 10):
		result += " %d" % i
		if (not i % n): result += 'V'
		
	return result
	
def Main():
	print("Welcome to the filter numbers program.")
	n = GetIntInput("Please enter the number you wish to be the divider: ")
	print(CreateDivisibleStr(n))
	input("Press any key to continue...")
	
if (__name__ == "__main__"): Main()