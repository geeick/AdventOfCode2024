def define_guard_path(file_path):

    try:
        with open(file_path, 'r') as file:
            board = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return 0
    except Exception as e:
        print(f"Error reading file: {e}")
        return 0

    rows, cols = len(board), len(board[0])

    count = 0
    for x in range(rows):
        for y in range(cols):
            if board[x][y] == '^' or '>' or '<' or 'V':  # Start search if the first letter matches
                posx = x
                posy = y
    while x < len(board) and y < len(board[0]):
            if board[posx][posy] == '^':
                if board[posx-1][posy] != '#':
                    board[posx-1][posy] = '^'
                    board[posx][posy] = 'X'
                    posx -= 1
                    count += 1
                elif board[posx-1][posy] == '#':
                    board[posx][posy] == '>'
            elif board[posx][posy] == '>':
                if board[posx][posy+1] != '#':
                    board[posx][posy+1] = '>'
                    board[posx][posy] = 'X'
                    posy += 1                    
                    count += 1
                elif board[posx-1][posy] == '#':
                    board[posx][posy] == 'v'
            elif board[posx][posy] == 'v':
                if board[posx+1][posy] != '#':
                    board[posx+1][posy] = 'v'
                    board[posx][posy] = 'X'
                    posx += 1
                    count += 1
                elif board[posx][posy-1] == '#':
                    board[posx][posy] == '<' 
            elif board[posx][posy] == '<':
                if board[posx][posy-1] != '#':
                    board[posx][posy-1] = '<'
                    board[posx][posy] = 'X'
                    posy -= 1
                    count += 1
                elif board[x][y-1] == '#':
                    board[x][y] == '^'                           

    print(board)
    print(f"Total guard steps: {count}")
    return count

file_path = "/Users/georgiaeick/Library/Mobile Documents/com~apple~TextEdit/Documents/AdventOfCode_Problem6.txt"
file_path_example = '/Users/georgiaeick/Library/Mobile Documents/com~apple~TextEdit/Documents/AdventOfCode_Problem6.txt'
print(define_guard_path(file_path_example))