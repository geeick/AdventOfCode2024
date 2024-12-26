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

def determineNodeLocations(antenna1, antenna2, board):
    nodes = set()
    type1, posx1, posy1 = antenna1
    type2, posx2, posy2 = antenna2
    distanceX, distanceY = determineAntennaDistance(antenna1, antenna2)
    x=0
    while abs(distanceX*x) < len(board) and abs(distanceY*x) < len(board[0]):
        nodeX = posx1 - distanceX*x
        nodeY = posy1 - distanceY*x
        nodes.add((nodeX, nodeY))
        x += 1
    return nodes

def determineAntennaNodes(board, antennas):
    result = set()
    rows, cols = len(board), len(board[0])

    for x in range(len(antennas)):
        for y in range(len(antennas)):
            if x != y:
                type1, posx1, pos1y = antennas[x]
                type2, posx2, posy2 = antennas[y]
                if type1 == type2:
                    nodes = determineNodeLocations(antennas[x], antennas[y], board)
                    for node in nodes:
                        nodeX, nodeY = node
                        if (0 <= nodeX < rows) and (0 <= nodeY < cols):
                            result.add((nodeX, nodeY))
    
    return result

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