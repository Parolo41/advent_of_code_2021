inputFile = open('D09P01.txt', 'r')
FileLines = inputFile.readlines()

def isLocalMinimum(grid, x, y):
	value = int(grid[y][x])
	
	if x > 0 and value >= int(grid[y][x - 1]):
		return False
	
	if x < len(grid[0]) - 1 and value >= int(grid[y][x + 1]):
		return False
	
	if y > 0 and value >= int(grid[y - 1][x]):
		return False
	
	if y < len(grid) - 1 and value >= int(grid[y + 1][x]):
		return False
	
	return True

def measureBasin(grid, x, y, checklist):
	checklist.append([x, y])
	
	if int(grid[y][x]) == 9:
		return 0
	
	count = 0
	
	if x > 0 and [x - 1, y] not in checklist:
		count += measureBasin(grid, x - 1, y, checklist)
	
	if y > 0 and [x, y - 1] not in checklist:
		count += measureBasin(grid, x, y - 1, checklist)
	
	if x < len(grid[0]) - 1 and  [x + 1, y] not in checklist:
		count += measureBasin(grid, x + 1, y, checklist)
	
	if y < len(grid) - 1 and [x, y + 1] not in checklist:
		count += measureBasin(grid, x, y + 1, checklist)
	
	return count + 1

heightMap = []

for line in FileLines:
	heightMap.append(list(line.strip()))

largestBasins = [0, 0, 0]
y = 0

while y < len(heightMap):
	x = 0
	
	while x < len(heightMap[y]):
		if isLocalMinimum(heightMap, x, y):
			basinSize = measureBasin(heightMap, x, y, [])
			
			i = 0
			
			while i < 3:
				if basinSize > largestBasins[i]:
					largestBasins.insert(i, basinSize)
					largestBasins.pop(3)
					break
				
				i += 1
		
		x += 1
	
	y += 1

total = largestBasins[0] * largestBasins[1] * largestBasins[2]

print("Largest basins: ", largestBasins)
print("Total: ", total)