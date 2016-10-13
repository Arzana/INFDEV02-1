from Utils import GetIntInput

def IsEven(n: int):
	return not n & 1
	
def Main():
	print("Welcome to the ever or odd program.")
	n = GetIntInput("Please enter a number: ")
	print("The number %d is %s." % (n, "even" if IsEven(n) else "odd"))
	input("Press any key to continue...")
	
if (__name__ == "__main__"): Main()