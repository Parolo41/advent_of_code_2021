inputFile = open('D08P01.txt', 'r')
FileLines = inputFile.readlines()

def findOutputDigit(digitMapping, outputSet):
	i = 0
	
	while i < 10:
		if outputSet == digitMapping[i]:
			return str(i)
		
		i += 1

finalResult = 0

for fileLine in FileLines:
	parts = fileLine.strip().split(" | ")
	digits = list(map(set, parts[0].split(" ")))
	output = list(map(set, parts[1].split(" ")))
	
	digitMapping = [set() for _ in range(10)]
	
	tempDigits = digits.copy()
	i = 0
	
	while i < len(tempDigits):
		if len(tempDigits[i]) == 2:
			digitMapping[1] = tempDigits[i]
			digits.remove(tempDigits[i])
		elif len(tempDigits[i]) == 3:
			digitMapping[7] = tempDigits[i]
			digits.remove(tempDigits[i])
		elif len(tempDigits[i]) == 4:
			digitMapping[4] = tempDigits[i]
			digits.remove(tempDigits[i])
		elif len(tempDigits[i]) == 7:
			digitMapping[8] = tempDigits[i]
			digits.remove(tempDigits[i])
		
		i += 1
	
	tempDigits = digits.copy()
	i = 0
	
	while i < len(tempDigits):
		if len(tempDigits[i]) == 5 and digitMapping[1] <= tempDigits[i]:
			digitMapping[3] = tempDigits[i]
			digits.remove(tempDigits[i])
			
		if (digitMapping[8] - tempDigits[i]) <= digitMapping[1]:
			digitMapping[6] = tempDigits[i]
			digits.remove(tempDigits[i])
		
		i += 1
	
	tempDigits = digits.copy()
	i = 0
	
	while i < len(tempDigits):
		if digitMapping[3] <= tempDigits[i]:
			digitMapping[9] = tempDigits[i]
			digits.remove(tempDigits[i])
			
			break
		
		i += 1
	
	tempDigits = digits.copy()
	i = 0
	
	while i < len(tempDigits):
		if len(tempDigits[i]) == 6:
			digitMapping[0] = tempDigits[i]
			digits.remove(tempDigits[i])
			
		if tempDigits[i] == (digitMapping[6] - (digitMapping[8] - digitMapping[9])):
			digitMapping[5] = tempDigits[i]
			digits.remove(tempDigits[i])
		
		i += 1
	
	digitMapping[2] = digits[0]
	
	outputString = ""
	
	for outputPosition in output:
		outputString = outputString + findOutputDigit(digitMapping, outputPosition)
	
	finalResult += int(outputString)

print("Final result: ", finalResult)