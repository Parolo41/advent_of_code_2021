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

heightMap = []

for line in FileLines:
	heightMap.append(list(line.strip()))

total = 0
y = 0

while y < len(heightMap):
	x = 0
	
	while x < len(heightMap[y]):
		if isLocalMinimum(heightMap, x, y):
			total += int(heightMap[y][x]) + 1
		
		x += 1
	
	y += 1

print("Total: ", total)