inputFile = open('D03P01.txt', 'r')
FileLines = inputFile.readlines()

bitCounts = [0] * (len(FileLines[0]) - 1)

for line in FileLines:
    i = 0
    
    while i < len(line):
        
        if line[i] == '1':
            bitCounts[i] += 1
        
        i += 1

bitValue = 1
valueCount = len(FileLines)

gammaRate = 0
epsilonRate = 0

i = len(bitCounts) - 1

while i >= 0:
    if bitCounts[i] >= valueCount / 2:
        gammaRate += bitValue
    else:
        epsilonRate += bitValue
    
    bitValue *= 2
    i -= 1

print("%d * %d = %d" % (gammaRate, epsilonRate, gammaRate * epsilonRate))