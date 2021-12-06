inputFile = open('D01P01.txt', 'r')
FileLines = inputFile.readlines()

increaseCount = 0
i = 1
previousDepth = int(FileLines[0])

while i < len(FileLines):
    intDepth = int(FileLines[i])
    
    if intDepth > previousDepth:
        increaseCount += 1
    
    previousDepth = intDepth;
    i += 1

print("The depth has increased %d times" % increaseCount)