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

file_path = "/Users/georgiaeick/Library/Mobile Documents/com~apple~TextEdit/Documents/AdventOfCode_Problem10.txt"
file_path_example = '/Users/georgiaeick/Library/Mobile Documents/com~apple~TextEdit/Documents/AdventOfCode_Problem10Ex.txt'

print(readFile(file_path_example))