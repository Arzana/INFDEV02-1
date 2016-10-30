def brange(length):
	start = length - 1
	while (start >= 1):
		yield start
		start -= 1
		
def drange(length):
	start = 0
	while (start < length - 1):
		yield start
		start += 1

# Executes a bubble style sort over the specified int32 numbers
def Sort_Bubble(numbers):
	n = len(numbers)
	temp = None
	
	for i in brange(n):
		for j in drange(n):
			if (numbers[j] > numbers[j + 1]):
				temp = numbers[j]
				numbers[j] = numbers[j + 1]
				numbers[j + 1] = temp