from Utils import GetIntInput

def IsPrime(n: int):
	if (n < 2 or not n & 1): return n == 2
	
	for m in range(3, n - 1):
		if (not n % m): return False

	return True
	
def Main():
	print("Welcome to the prime number program.")
	n = GetIntInput("Please enter the number you wish to be examined: ")
	print("%d is%s a prime number!" % (n, '' if IsPrime(n) else " not"))
	input("Press any key to continue...")
	
if (__name__ == "__main__"): Main()