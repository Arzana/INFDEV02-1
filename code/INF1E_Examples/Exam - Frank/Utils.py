def GetIntInput(msg: str):
	result = None
	while (result == None):
		try:
			result = int(input(msg))
		except:
			pass
			
	return result
	
def Populate(char: chr, amount: int):
	result = ''
	
	for i in range(amount):
		result += char
		
	return result;