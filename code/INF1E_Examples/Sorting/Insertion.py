# Executes a insertion style sort over the specified int32 numbers
def Sort_Insertion(numbers):
	for i in range(1, len(numbers)):
		newI = i
		for j in range(i - 1, -1, -1):
			if (numbers[j] > numbers[i]): newI = j
			
		if (newI != i): numbers.insert(newI, numbers.pop(i))