inputFile = open('D03P01.txt', 'r')
FileLines = inputFile.readlines()

def getCommonValue(lines, position):
    bitCount = 0
    
    for line in lines:
        if line[position] == '1':
            bitCount += 1
    
    if bitCount >= len(lines) / 2:
        commonValue = '1'
    else:
        commonValue = '0'
    
    return commonValue

valueCount = len(FileLines)

oxygenList = FileLines.copy()
co2List = FileLines.copy()

i = 0

while len(oxygenList) > 1 or len(co2List) > 1:
    commonValue = getCommonValue(oxygenList, i)
    
    j = 0
    
    while j < len(oxygenList) and len(oxygenList) > 1:
        if oxygenList[j][i] != commonValue:
            oxygenList.pop(j)
        else:
            j += 1
    
    commonValue = getCommonValue(co2List, i)
    
    j = 0
    
    while j < len(co2List) and len(co2List) > 1:
        if co2List[j][i] == commonValue:
            co2List.pop(j)
        else:
            j += 1
    
    i += 1

oxygenValue = int(oxygenList[0], 2)
co2Value = int(co2List[0], 2)

print("%d * %d = %d" % (oxygenValue, co2Value, oxygenValue * co2Value))