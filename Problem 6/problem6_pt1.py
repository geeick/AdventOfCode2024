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

    for x in range(rows - 1):
        for y in range(cols):
            if board[x][y] == '^' or board[x][y] == '>' or board[x][y] == '<' or board[x][y] == 'V':
                posx = x
                posy = y
                break
            
    while posx < len(board) -1 and posy < len(board[0]) -1 and x >= 0 and y >= 0: 
            if board[posx][posy] == '^':
                if board[posx-1][posy] != '#':

                    if board[posx-1][posy] != 'X':
                        count += 1

                    board[posx-1][posy] = '^'
                    board[posx][posy] = 'X'

                    posx -= 1

                elif board[posx-1][posy] == '#':
                    board[posx][posy] = '>'

            elif board[posx][posy] == '>':
                if board[posx][posy+1] != '#':

                    if board[posx][posy+1] != 'X':
                        count += 1

                    board[posx][posy+1] = '>'
                    board[posx][posy] = 'X'

                    posy += 1                    
                    
                elif board[posx][posy+1] == '#':
                    board[posx][posy] = 'v'

            elif board[posx][posy] == 'v':
                if board[posx+1][posy] != '#':

                    if board[posx+1][posy] != 'X':
                        count += 1

                    board[posx+1][posy] = 'v'
                    board[posx][posy] = 'X'

                    posx += 1

                elif board[posx+1][posy] == '#':
                    board[posx][posy] = '<' 
            elif board[posx][posy] == '<':

                if board[posx][posy-1] != 'X':
                        count += 1

                if board[posx][posy-1] != '#':
                    board[posx][posy-1] = '<'
                    board[posx][posy] = 'X'

                    posy -= 1

                elif board[posx][posy-1] == '#':
                    board[posx][posy] = '^'                           

    print(f"Total guard steps: {count}")
    return count

file_path = "/Users/georgiaeick/Library/Mobile Documents/com~apple~TextEdit/Documents/AdventOfCode_Problem6.txt"
file_path_example = '/Users/georgiaeick/Library/Mobile Documents/com~apple~TextEdit/Documents/AdventOfCode_Problem6Ex.txt'
print(define_guard_path(file_path))