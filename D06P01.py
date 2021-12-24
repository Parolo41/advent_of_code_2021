inputFile = open('D06P01.txt', 'r')
FileLines = inputFile.readlines()

fishAges = FileLines[0].split(",")

fishByAge = [0] * 7
newbornFish = [0] * 7

for fishAge in fishAges:
	fishByAge[int(fishAge)] += 1

i = 0

while i < 80:
	newbornFish[(i + 2) % 7] = fishByAge[i % 7]
	fishByAge[i % 7] += newbornFish[i % 7]
	newbornFish[i % 7] = 0
	
	i += 1

fishCount = 0
i = 0

while i < 7:
	fishCount += fishByAge[i]
	fishCount += newbornFish[i]
	
	i += 1

print("Total fish: ", fishCount)