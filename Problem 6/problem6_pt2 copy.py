def define_guard_path(file_path):

    try:
        with open(file_path, 'r') as file:
            board = [list(line.strip()) for line in file.readlines()]
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return 0
    except Exception as e:
        print(f"Error reading file: {e}")
        return 0

    rows, cols = len(board), len(board[0])
    count = 0
    posx, posy = -1, -1

    for x in range(rows):
        for y in range(cols):
            if board[x][y] == '^':
                posx = x
                posy = y
                dir = "UP"
            if board[x][y] == '>' :
                posx = x
                posy = y
                dir = "RIGHT"
            if board[x][y] == '<' :
                posx = x
                posy = y
                dir = "LEFT"
            if board[x][y] == 'V':
                posx = x
                posy = y
                dir = "DOWN"
                break
        if posx != -1:  
            break

    seen = set() 

    def loop_detected(posx, posy, count, dir, recursion):
        while 0 < posx < rows -1 and 0 < posy < cols - 1  and (recursion < 15):
            if (posx, posy, dir) in seen:
                return True
            else:
                while 0 < posx < rows -1 and 0 < posy < cols - 1:
                    posx, posy, count, dir, recursion = search_next_hash(posx, posy, count, dir, recursion)   
                    recursion += 1
                    if (loop_detected(posx, posy, count, dir, recursion) == True):
                         return True
        return False
            
    def move(posx, posy, dir):
        if dir == "UP":
            if board[posx-1][posy] != '#':
                board[posx-1][posy] = '^'
                board[posx][posy] = 'X'
                seen.add((posx, posy, "UP"))
                posx -= 1
            elif board[posx-1][posy] == '#':
                dir = "RIGHT"
            return posx, posy, dir

        if dir == "RIGHT":
            if board[posx][posy+1] != '#':
                    board[posx][posy+1] = '>'
                    board[posx][posy] = 'X'
                    seen.add((posx, posy, "RIGHT"))
                    posy += 1                    
            elif board[posx][posy+1] == '#':
                dir = "DOWN"

        if dir == "DOWN":
            if board[posx+1][posy] != '#':
                    board[posx+1][posy] = 'v'
                    board[posx][posy] = 'X'
                    seen.add((posx, posy, "DOWN"))
                    posx += 1
            elif board[posx+1][posy] == '#':
                dir = "LEFT"

        if dir == "LEFT":
            if board[posx][posy-1] != '#':
                        board[posx][posy-1] = '<'
                        board[posx][posy] = 'X'
                        seen.add((posx, posy, "LEFT"))
                        posy -= 1
            elif board[posx][posy-1] == '#':
                dir = "UP"
        
        return posx, posy, dir

    def search_next_hash(posx, posy, count, dir, recursion):
        if dir == "UP":
            for column in range (posy, cols):
                if board[posx-1][column] == '#':
                    return posx, column, count, dir, recursion

        elif dir == "RIGHT":
                for row in range (posx, rows):
                    if board[row][posy+1] == '#':
                        return row, posy, count, dir, recursion


        elif dir == "DOWN":
                for column in range (posy, -1, -1):
                    if board[posx+1][column] == '#':
                        return posx, column, count, dir, recursion

        elif dir == "LEFT":
                for row in range (posx, -1, -1):
                    if board[row][posy -1] == '#':
                        return row, posy, count, dir, recursion


    while 0 < posx < rows -1 and 0 < posy < cols - 1:
        recursion = 0           
        posx, posy, count, dir, recursion = search_next_hash(posx, posy, count, dir, recursion)   
        posx, posy, dir = move(posx, posy, dir)

    result = count
    return result

file_path = "/Users/georgiaeick/Library/Mobile Documents/com~apple~TextEdit/Documents/AdventOfCode_Problem6.txt"
file_path_example = '/Users/georgiaeick/Library/Mobile Documents/com~apple~TextEdit/Documents/AdventOfCode_Problem6Ex.txt'
print(define_guard_path(file_path_example))