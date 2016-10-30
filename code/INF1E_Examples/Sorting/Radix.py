# Executes a radix style sort over the specified int32 numbers
def Sort_Radix(numbers):
	zeros = []
	ones = []
	
	for b in range(32):
		mask = 1 << b
		for i in range(len(numbers)):
			cur = numbers[i]
			if (cur & mask): ones.append(cur)
			else: zeros.append(cur)
			
		numbers.clear()
		numbers.extend(zeros)
		numbers.extend(ones)
		zeros.clear()
		ones.clear()