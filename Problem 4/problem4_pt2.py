def count_xmas_in_grid(file_path):
    def is_valid_position(x, y, rows, cols):
        return 0 <= x < rows and 0 <= y < cols

    def search_in_direction(board, x, y, dx, dy, word):
        rows, cols = len(board), len(board[0])
        for i in range(len(word)):
            nx, ny = x + i * dx, y + i * dy
            if not is_valid_position(nx, ny, rows, cols) or board[nx][ny] != word[i]:
                return False
        return True

    # Directions: (dx, dy)
    directions = [
        (0, 1),   # right
        (0, -1),  # left
        (1, 0),   # down
        (-1, 0),  # up
        (1, 1),   # down-right
        (-1, -1), # up-left
        (1, -1),  # down-left
        (-1, 1)   # up-right
    ]

    try:
        with open(file_path, 'r') as file:
            board = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return 0
    except Exception as e:
        print(f"Error reading file: {e}")
        return 0

    count = 0

    rows, cols = len(board), len(board[0])

    for x in range(rows - 1):
        for y in range(cols - 1):
            if board[x][y] :  # Start search if the first letter matches
                    if (board[x-1][y-1] == 'M' and
                        board[x-1][y+1] == 'S' and
                        board[x+1][y-1] == 'M' and
                        board[x+1][y+1] == 'S'):
                        count += 1
                    if (board[x-1][y-1] == 'S' and
                        board[x-1][y+1] == 'M' and
                        board[x+1][y-1] == 'S' and
                        board[x+1][y+1] == 'M'):
                        count += 1
                    if (board[x-1][y-1] == 'M' and
                        board[x-1][y+1] == 'M' and
                        board[x+1][y-1] == 'S' and
                        board[x+1][y+1] == 'S'):
                        count += 1
                    if (board[x-1][y-1] == 'S' and
                        board[x-1][y+1] == 'S' and
                        board[x+1][y-1] == 'M' and
                        board[x+1][y+1] == 'M'):
                        count += 1

    print(f"Total 'XMAS' occurrences: {count}")
    return count

file_path = "/Users/georgiaeick/Library/Mobile Documents/com~apple~TextEdit/Documents/AdventOfCode_Problem4.txt"
file_path_example = '/Users/georgiaeick/Library/Mobile Documents/com~apple~TextEdit/Documents/AdventOfCode_Problem3Ex.txt'
print(count_xmas_in_grid(file_path))

