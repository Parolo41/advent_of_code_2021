inputFile = open('D04P01.txt', 'r')
FileLines = inputFile.readlines()

def isLineComplete(checkCard, y):
    i = 0
    
    while i < 5:
        if not checkCard[y][i]:
            return False
        
        i += 1
    
    return True

def isColumnComplete(checkCard, x):
    i = 0
    
    while i < 5:
        if not checkCard[i][x]:
            return False
        
        i += 1
    
    return True

def getUncheckedSum(bingoCard):
    uncheckedSum = 0
    i = 0
    
    while i < 5:
        j = 0
        
        while j < 5:
            if not bingoCard["check"][i][j]:
                uncheckedSum += int(bingoCard["values"][i][j])
            
            j += 1
        
        i += 1
    
    return uncheckedSum

bingoNumbers = FileLines[0].strip().split(',')
bingoCards = []

i = 2

while i < len(FileLines):
    bingoCard = {}
    bingoCardRows = [0] * 5
    
    j = 0
    
    while j < 5:
        f = filter(None, FileLines[i+j].strip().split(' '))
        bingoCardRows[j] = list(f)
        
        j += 1
    
    bingoCard["values"] = bingoCardRows
    bingoCard["check"] = [[False] * 5, [False] * 5, [False] * 5, [False] * 5, [False] * 5]
    bingoCards.append(bingoCard)
    
    i += 6

cardIndex = 0
latestVictoryTurn = 0
latestVictoryCardIndex = 0

while cardIndex < len(bingoCards):
    turnNumber = 0
    bingoCard = bingoCards[cardIndex]
    
    for bingoNumber in bingoNumbers:
        i = 0
        
        while i < 5 and turnNumber >= 0:
            j = 0
            
            while j < 5 and turnNumber >= 0:
                if bingoCard["values"][i][j] == bingoNumber:
                    bingoCard["check"][i][j] = True
                    
                    if isLineComplete(bingoCard["check"], i) or isColumnComplete(bingoCard["check"], j):
                        if turnNumber > latestVictoryTurn:
                            latestVictoryTurn = turnNumber
                            latestVictoryCardIndex = cardIndex
                        
                        turnNumber = -1
                
                j += 1
            
            i += 1
        
        if turnNumber < 0:
            break
        
        turnNumber += 1
    
    cardIndex += 1

uncheckedSum = getUncheckedSum(bingoCards[latestVictoryCardIndex])

print("%s * %d = %d" % (bingoNumbers[latestVictoryTurn], uncheckedSum, int(bingoNumbers[latestVictoryTurn]) * uncheckedSum))