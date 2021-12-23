inputFile = open('D05P01.txt', 'r')
FileLines = inputFile.readlines()

def getVectorData(vectorString):
	points = vectorString.split(" -> ")
	point1 = points[0].split(",")
	point2 = points[1].split(",")
	
	vectorDict = {}
	
	vectorDict["x1"] = int(point1[0])
	vectorDict["y1"] = int(point1[1])
	vectorDict["x2"] = int(point2[0])
	vectorDict["y2"] = int(point2[1])
	
	return vectorDict

positionGrid = []
twoOrMoreCount = 0

i = 0

while i < 1000:
	positionGrid.append([0] * 1000)
	i += 1

for vectorString in FileLines:
	vector = getVectorData(vectorString)
	
	startX = vector["x1"]
	endX = vector["x2"]

	startY = vector["y1"]
	endY = vector["y2"]

	while True:
		positionGrid[startX][startY] += 1

		if positionGrid[startX][startY] == 2:
			twoOrMoreCount += 1

		if startX == endX and startY == endY:
			break

		startX = startX + 1 if startX < endX else max(endX, startX - 1)
		startY = startY + 1 if startY < endY else max(endY, startY - 1)
			
print("Positions with 2 or more: ", twoOrMoreCount)