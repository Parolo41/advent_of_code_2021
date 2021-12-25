inputFile = open('D08P01.txt', 'r')
FileLines = inputFile.readlines()

uniqueDigits = 0

for fileLine in FileLines:
	parts = fileLine.strip().split(" | ")
	digits = parts[1].split(" ")
	
	print(parts)
	print(digits)
	
	for digit in digits:
		segLen = len(digit)
		
		if segLen == 2 or segLen == 3 or segLen == 4 or segLen == 7:
			uniqueDigits += 1

print("Unique digits", uniqueDigits)