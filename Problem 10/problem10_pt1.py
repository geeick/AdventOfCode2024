def copyMap(map):
    mapCopy = []
    rows, cols = len(map), len(map[0])
    for row in range(rows):
        mapCols = []
        for col in range(cols):
            mapCols.append(map[row][col])
        mapCopy.append(mapCols)
    return mapCopy


def readFile(file_path):
    try:
        with open(file_path, 'r') as file:
            map = [list(line.strip()) for line in file.readlines()]
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return 0
    except Exception as e:
        print(f"Error reading file: {e}")
        return 0
    return map

def getTrailheads(map):
    rows, cols = len(map), len(map[0])
    trailheads = set()
    for x in range(rows):
        for y in range(cols):
            if map[x][y] == '0':
                trailheads.add((x, y))
    return trailheads
 
def getSideBlocks(map, x, y):
    sideBlocks = set()
    if 0 < x:
        sideBlocks.add((x-1, y))
    if x < len(map) -1:
        sideBlocks.add((x+1, y))
    if  0 < y:
        sideBlocks.add((x, y-1))
    if y < len(map[0]) -1:
        sideBlocks.add((x, y+1))
    return sideBlocks

def makeMove(map, x, y):
    paths = set()
    movable = False
    sideBlocks = getSideBlocks(map, x, y)
    for sideBlock in sideBlocks:
        sideX, sideY = sideBlock
        if map[sideX][sideY].isdigit() and map[x][y].isdigit() and int(map[sideX][sideY]) == int(map[x][y]) + 1:
            paths.add((sideX, sideY))
            movable = True
    return movable, paths

def trailHeadScore(map, x, y, score, seen):
    prev = int(map[x][y])
    movable, paths = makeMove(map, x, y)
    mapCopy = copyMap(map)
    mapCopy[x][y] = 'X'
    for path in paths:
        x, y = path
        if movable == False:
            break

        if prev == 8 and int(map[x][y]) == 9 and (x,y) not in seen:
            score += 1
            seen.add((x, y))
        else:
            score, seen = trailHeadScore(mapCopy, x, y, score, seen)
    return score, seen

def addSum(map, trailheads):
    total = 0
    for trailhead in trailheads:
        seen = set()
        x, y = trailhead
        score, seen = trailHeadScore(map, x, y, 0, seen)
        total += score
    
    return total
    



file_path = "/Users/georgiaeick/Library/Mobile Documents/com~apple~TextEdit/Documents/AdventOfCode_Problem10.txt"
file_path_example = '/Users/georgiaeick/Library/Mobile Documents/com~apple~TextEdit/Documents/AdventOfCode_Problem10Ex.txt'

map = readFile(file_path)
trailheads = getTrailheads(map)
print (addSum(map, trailheads))
