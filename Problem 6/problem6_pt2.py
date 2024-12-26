loops = set()

def is_loop(file_path, posx, posy, dir, seen):
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
    seencopy = set()

    if 0 < posx < rows -1 and 0 < posy < cols -1:
        match dir:
            case "UP":
                board[posx - 1][posy] = "#"
            case "RIGHT":
                board[posx][posy + 1] = "#"
            case "DOWN":
                board[posx + 1][posy] = "#"
            case "LEFT":
                board[posx][posy - 1] = "#"

    def move(posx, posy, dir):
        if dir == "UP":
            if board[posx-1][posy] != '#':
                board[posx-1][posy] = '^'
                board[posx][posy] = 'X'
                seencopy.add((posx, posy, "UP"))
                posx -= 1
            elif board[posx-1][posy] == '#':
                dir = "RIGHT"
            return posx, posy, dir, seencopy

        if dir == "RIGHT":
            if board[posx][posy+1] != '#':
                board[posx][posy+1] = '>'
                board[posx][posy] = 'X'
                seencopy.add((posx, posy, "RIGHT"))
                posy += 1                    
            elif board[posx][posy+1] == '#':
                dir = "DOWN"

        if dir == "DOWN":
            if board[posx+1][posy] != '#':
                board[posx+1][posy] = 'v'
                board[posx][posy] = 'X'
                seencopy.add((posx, posy, "DOWN"))
                posx += 1
            elif board[posx+1][posy] == '#':
                dir = "LEFT"

        if dir == "LEFT":
            if board[posx][posy-1] != '#':
                    board[posx][posy-1] = '<'
                    board[posx][posy] = 'X'
                    seencopy.add((posx, posy, "LEFT"))
                    posy -= 1
            elif board[posx][posy-1] == '#':
                dir = "UP"
        
        return posx, posy, dir, seencopy

    while 0 < posx < rows -1 and 0 < posy < cols - 1:
        posx, posy, dir, seencopy = move(posx, posy, dir)
        if (posx, posy, dir) in seencopy:
            return True   
    return False

def count_loops(file_path):
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
    posx, posy = -1, -1
    count = 0
    seen = set()

    for x in range(rows):
        for y in range(cols):
            if board[x][y] == '^':
                posx = x
                posy = y
                dir = "UP"
                break
            if board[x][y] == '>' :
                posx = x
                posy = y
                dir = "RIGHT"
                break
            if board[x][y] == '<' :
                posx = x
                posy = y
                dir = "LEFT"
                break
            if board[x][y] == 'v':
                posx = x
                posy = y
                dir = "DOWN"
                break
        if posx != -1:  
            break
        
    while 0 < posx < rows -1 and 0 < posy < cols - 1:
        if dir == "UP":
            if board[posx-1][posy] != '#':
                board[posx-1][posy] = '^'
                board[posx][posy] = 'X'
                posx -= 1
                if is_loop(file_path, posx, posy, "UP", seen) and (posx, posy) not in loops:
                    count += 1
                    loops.add((posx -1, posy))
                seen.add((posx, posy, dir))
            elif board[posx-1][posy] == '#':
                dir = 'RIGHT'
                if is_loop(file_path, posx, posy, "RIGHT", seen) and (posx, posy) not in loops:
                    count += 1
                    loops.add((posx, posy +1))

        elif dir == "RIGHT":
            if board[posx][posy+1] != '#':
                board[posx][posy+1] = '>'
                board[posx][posy] = 'X'
                posy += 1
                if is_loop(file_path, posx, posy, "RIGHT", seen) and (posx, posy) not in loops:
                    count += 1
                    loops.add((posx, posy +1))
                seen.add((posx, posy, dir))
            elif board[posx][posy+1] == '#':
                dir = 'DOWN'
                if is_loop(file_path, posx, posy, "DOWN", seen) and (posx, posy) not in loops:
                    count += 1
                    loops.add((posx +1, posy))

        elif dir == "DOWN":
            if board[posx+1][posy] != '#':
                board[posx+1][posy] = 'v'
                board[posx][posy] = 'X'
                posx += 1
                if is_loop(file_path, posx, posy, "DOWN", seen)  and (posx, posy) not in loops:
                    count += 1
                    loops.add((posx + 1, posy))
                seen.add((posx, posy, dir))
            elif board[posx+1][posy] == '#':
                dir = 'LEFT' 
                if is_loop(file_path, posx, posy, "LEFT", seen) and (posx, posy) not in loops:
                    count += 1
                    loops.add((posx, posy -1))

        elif dir == "LEFT":
            if board[posx][posy-1] != '#':
                board[posx][posy-1] = '<'
                board[posx][posy] = 'X'
                posy -= 1
                if is_loop(file_path, posx, posy, "LEFT", seen) and (posx, posy) not in loops:
                    count += 1
                    loops.add((posx, posy - 1))
                seen.add((posx, posy, dir))

            elif board[posx][posy-1] == '#':
               dir = 'UP'                   
               if is_loop(file_path, posx, posy, "UP", seen) and (posx, posy) not in loops:
                    count += 1
                    loops.add((posx -1, posy))        
    return count
    
file_path = "/Users/georgiaeick/Library/Mobile Documents/com~apple~TextEdit/Documents/AdventOfCode_Problem6.txt"
file_path_example = '/Users/georgiaeick/Library/Mobile Documents/com~apple~TextEdit/Documents/AdventOfCode_Problem6Ex.txt'

count_loops(file_path)
print(len(loops))