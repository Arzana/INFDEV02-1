# Executes a selection style sort over the specified int32 numbers
def Sort_Selection(numbers):
	n = len(numbers)
	temp = None
	
	for i in range(n - 1):
		min = i
		for j in range(i + 1, n):
			if (numbers[j] < numbers[min]): min = j
			
		if (min != i):
			temp = numbers[i]
			numbers[i] = numbers[min]
			numbers[min] = temp