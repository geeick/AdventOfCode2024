def readMap(file_path):
    try:
        with open(file_path, 'r') as file:
            board = [list(line.strip()) for line in file.readlines()]
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return 0
    except Exception as e:
        print(f"Error reading file: {e}")
        return 0
    return board

def determineAntennas(board):
    rows, cols = len(board), len(board[0])

    antennas = []

    for row in range(rows):
        for col in range(cols):
            if board[row][col] != ".":
                antennas.append([board[row][col], row, col])

    return antennas 

def determineAntennaDistance(antenna1, antenna2):
    type1, posx1, posy1 = antenna1
    type2, posx2, posy2 = antenna2
    distancex = posx2 - posx1
    distancey = posy2 - posy1
    return distancex, distancey

def determineNodeLocation(antenna1, antenna2):
    type1, posx1, posy1 = antenna1
    type2, posx2, posy2 = antenna2
    distanceX, distanceY = determineAntennaDistance(antenna1, antenna2)
    nodeX = posx1 - distanceX
    nodeY = posy1 - distanceY
    return nodeX, nodeY

def determineAntennaNodes(board, antennas):
    nodes = set()
    rows, cols = len(board), len(board[0])

    for x in range(len(antennas)):
        for y in range(len(antennas)):
            if x != y:
                type1, posx1, pos1y = antennas[x]
                type2, posx2, posy2 = antennas[y]
                if type1 == type2:
                    nodeX, nodeY = determineNodeLocation(antennas[x], antennas[y])
                    if (0 <= nodeX < rows) and (0 <= nodeY < cols):
                        nodes.add((nodeX, nodeY))
    
    return nodes

def boardWithAntennas(board, nodes):
    rows, cols = len(board), len(board[0])
    for x in range(rows):
        for y in range(cols):
            if (x, y) in nodes:
                board[x][y] = '#'
    return board

    

file_path = "/Users/georgiaeick/Library/Mobile Documents/com~apple~TextEdit/Documents/AdventOfCode_Problem8.txt"
file_path_example = '/Users/georgiaeick/Library/Mobile Documents/com~apple~TextEdit/Documents/AdventOfCode_Problem8Ex.txt'

board = readMap(file_path)
antennas = determineAntennas(board)
nodes = determineAntennaNodes(board, antennas)
print(len(nodes))