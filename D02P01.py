inputFile = open('D02P01.txt', 'r')
FileLines = inputFile.readlines()

horizontalPos = 0
verticalPos = 0

for line in FileLines:
    values = line.split(" ")
    
    if values[0] == "forward":
        horizontalPos += int(values[1])
    if values[0] == "up":
        verticalPos -= int(values[1])
    if values[0] == "down":
        verticalPos += int(values[1])

print("%d * %d = %d" % (horizontalPos, verticalPos, horizontalPos * verticalPos))