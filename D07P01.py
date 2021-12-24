inputFile = open('D07P01.txt', 'r')
FileLines = inputFile.readlines()

crabPositions = list(map(int, FileLines[0].split(",")))

previousFuelUsed = 0
i = 0

while True:
	fuelUsed = 0
	
	for crabPosition in crabPositions:
		fuelUsed += abs(i - crabPosition)
	
	if fuelUsed > previousFuelUsed and previousFuelUsed > 0:
		break
	
	previousFuelUsed = fuelUsed
	
	i += 1

print("Fuel used: ", previousFuelUsed)