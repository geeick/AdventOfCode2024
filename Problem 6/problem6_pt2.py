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

    def translate_dir(char):
        if char == '^':
            return "UP"
        if char == '>':
            return "RIGHT"  
        if char == 'v':
            return "DOWN"
        if char == '<':
            return "LEFT"
        else:
            return char
          
    dir = "UP"
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

    def search_next_hash(posx, posy, count, dir):
        if translate_dir(board[posx][posy]) == "UP":
            if board[posx-1][posy] != '#':
                for column in range (posy, cols):
                    if board[posx-1][column] == '#':
                        if (posx-1, column -1, "DOWN") in seen:
                            count += 1
                            break
                        else:
                            search_next_hash(posx-1, column -1, count, "RIGHT")
                board[posx-1][posy] = '^'
                board[posx][posy] = 'X'
                seen.add((posx, posy, "UP"))
                posx -= 1
            elif board[posx-1][posy] == '#':
                board[posx][posy] = '>'

        elif translate_dir(board[posx][posy]) == "RIGHT":
            if board[posx][posy+1] != '#':
                for row in range (posx, rows):
                    if board[row][posy+1] == '#':
                        if (row -1, posy+1, "LEFT") in seen:
                            count += 1
                            break
                        else:
                            search_next_hash(row-1, posy +1, count, "DOWN")
                board[posx][posy+1] = '>'
                board[posx][posy] = 'X'
                seen.add((posx, posy, "RIGHT"))
                posy += 1                    
            elif board[posx][posy+1] == '#':
                board[posx][posy] = 'v'

        elif translate_dir(board[posx][posy]) == "DOWN":
            if board[posx+1][posy] != '#':
                for column in range (posy, -1, -1):
                    if board[posx+1][column] == '#':
                        if (posx+1, column +1, "UP") in seen:
                            count += 1
                            break
                        else:
                            search_next_hash(posx+1, column+1, count,  "LEFT")
                board[posx+1][posy] = 'v'
                board[posx][posy] = 'X'
                seen.add((posx, posy, "DOWN"))
                posx += 1
            elif board[posx+1][posy] == '#':
                board[posx][posy] = '<' 

        elif translate_dir(board[posx][posy]) == "LEFT":
            if board[posx][posy-1] != '#':
                for row in range (posx, -1, -1):
                    if board[row][posy -1] == '#':
                        if (row + 1, posy -1, "RIGHT") in seen:
                            count += 1
                            break
                        else:
                            search_next_hash(row +1, posy -1, count, "UP")
            if board[posx][posy-1] != '#':
                board[posx][posy-1] = '<'
                board[posx][posy] = 'X'
                seen.add((posx, posy, "LEFT"))
                posy -= 1
            elif board[posx][posy-1] == '#':
                board[posx][posy] = '^'

        return posx, posy, count

    while 0 < posx < rows -1 and 0 < posy < cols - 1:
        posx, posy, count = search_next_hash(posx, posy, count, dir)       

    for line in board:
        for char in line:
            print(char, end = "")
        print('\n')             

    result = count
    return result

file_path = "/Users/georgiaeick/Library/Mobile Documents/com~apple~TextEdit/Documents/AdventOfCode_Problem6.txt"
file_path_example = '/Users/georgiaeick/Library/Mobile Documents/com~apple~TextEdit/Documents/AdventOfCode_Problem6Ex.txt'
print(define_guard_path(file_path))