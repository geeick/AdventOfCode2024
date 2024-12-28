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

def copyMap(map):
    mapCopy = []
    rows, cols = len(map), len(map[0])
    for row in range(rows):
        mapCols = []
        for col in range(cols):
            mapCols.append(map[row][col])
        mapCopy.append(mapCols)
    return mapCopy

def getPerimeter(map, x, y):
    sideBlocks = []
    if 0 < x and (map[x-1][y] == map[x][y] or map[x-1][y] == map[x][y].lower()):
        sideBlocks.append((x-1, y))
    if x < len(map) -1 and (map[x+1][y] == map[x][y] or map[x+1][y] == map[x][y].lower()):
        sideBlocks.append((x+1, y))
    if  0 < y and (map[x][y-1] == map[x][y] or map[x][y-1] == map[x][y].lower()):
        sideBlocks.append((x, y-1))
    if y < len(map[0]) -1 and (map[x][y+1] == map[x][y] or map[x][y+1]== map[x][y].lower()):
        sideBlocks.append((x, y+1))
    
    perimeter = 4-len(sideBlocks)

    return perimeter

def makeRegion(map):
    rows, cols = len(map), len(map[0])
    groups = []
    for row in range(rows):
        for col in range(cols):
            if map[row][col] not in groups:
                groups.append(map[row][col])      

        def dfs(x, y, letter):
            region = []
            stack = [(x, y)]
            seen.add((x, y))
            region.append((x, y))
            
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            
            while stack:
                cx, cy = stack.pop()
                
                for dx, dy in directions:
                    nx, ny = cx + dx, cy + dy
                    if 0 <= nx < len(map) and 0 <= ny < len(map[0]) and (nx, ny) not in seen and map[nx][ny] == letter:
                        seen.add((nx, ny))
                        region.append((nx, ny))
                        stack.append((nx, ny))
            
            return region

        rows, cols = len(map), len(map[0])
        seen = set() 
        regions = []

        for i in range(rows):
            for j in range(cols):
                if (i, j) not in seen:
                    letter = map[i][j]
                    region = dfs(i, j, letter)
                    regions.append(region)

    return regions

def deleteInside(map):
    mapCopy = copyMap(map)
    rows, cols = len(map), len(map[0])
    for row in range(rows-1):
        for col in range(cols-1):
            if map[row][col] == map[row -1][col] and map[row][col] == map[row +1][col] and map[row][col] == map[row][col-1] and map[row][col] == map[row ][col+1]:
                mapCopy[row][col] = mapCopy[row][col].lower()
    return mapCopy


def countValue(map, region, group):
    perimeter = 0
    area = 0
    rows, cols = len(map), len(map[0])
    for plant in region:
        x, y = plant
        if map[x][y] == group:
            perimeter += getPerimeter(map, x, y)
        if map[x][y] == group.lower() or map[x][y] == group:
            area += 1
    total = area*perimeter
    print(total)
    return total

def countTotal(map):
    regions = makeRegion(map)
    map = deleteInside(map)
    total = 0
    for region in regions:
        x, y = region[0]
        group = map[x][y].upper()
        total+= countValue (map, region, group)
    return total
      
  
file_path = "/Users/georgiaeick/Library/Mobile Documents/com~apple~TextEdit/Documents/AdventOfCode_Problem12.txt"
file_path_example = "/Users/georgiaeick/Library/Mobile Documents/com~apple~TextEdit/Documents/AdventOfCode_Problem12Ex.txt"

map = readFile(file_path)
print(countTotal(map))

#1376900 is too low

