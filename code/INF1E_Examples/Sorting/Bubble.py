# Executes a bubble style sort over the specified int32 numbers
def Sort_Bubble(numbers):
	n = len(numbers) - 1
	temp = None
	
	for i in range(n, 0, -1):
		for j in range(n):
			if (numbers[j] > numbers[j + 1]):
				temp = numbers[j]
				numbers[j] = numbers[j + 1]
				numbers[j + 1] = temp