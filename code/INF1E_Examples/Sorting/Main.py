from Bubble import Sort_Bubble
from Selection import Sort_Selection
from Insertion import Sort_Insertion
from Radix import Sort_Radix

from random import randint
from traceback import print_exc

# Creates a array with a specified fixed length and 
# filled with random int32 values
# ranging from zero to a specified maximum or 2147483647
def CreateRandomNubers(length:int, max = 0x7FFFFFFF):
	result = []
	for i in range(length):
		result.append(randint(0x0, max))
	return result

def Main():
	numbers = CreateRandomNubers(16, 16);
	
	print(numbers)
	Sort_Radix(numbers)
	print(numbers)
	
if (__name__ == "__main__"): 
	try: Main()
	except: print_exc()
	input("Press any key to continue...")