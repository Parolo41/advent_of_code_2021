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
	
	if vector["x1"] == vector["x2"] or vector["y1"] == vector["y2"]:
		startX = min(vector["x1"], vector["x2"])
		endX = max(vector["x1"], vector["x2"])
		
		startY = min(vector["y1"], vector["y2"])
		endY = max(vector["y1"], vector["y2"])
		
		while True:
			positionGrid[startX][startY] += 1
			
			if positionGrid[startX][startY] == 2:
				twoOrMoreCount += 1
			
			if startX == endX and startY == endY:
				break
			
			startX = min(endX, startX + 1)
			startY = min(endY, startY + 1)
			
print("Positions with 2 or more: ", twoOrMoreCount)