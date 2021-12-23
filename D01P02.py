inputFile = open('D01P01.txt', 'r')
FileLines = inputFile.readlines()

increaseCount = 0
i = 1
previousDepth = int(FileLines[0]) + int(FileLines[1]) + int(FileLines[2])

while i < len(FileLines) - 2:
    intDepth = int(FileLines[i]) + int(FileLines[i+1]) + int(FileLines[i+2])
    
    if intDepth > previousDepth:
        increaseCount += 1
    
    previousDepth = intDepth;
    i += 1

print("The depth has increased %d times" % increaseCount)