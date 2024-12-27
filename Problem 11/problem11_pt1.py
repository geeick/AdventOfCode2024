def readCode(file_path):
    try:
        with open(file_path, 'r') as file:
            code = file.read()
            code = code.split(" ")
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return 0
    except Exception as e:
        print(f"Error reading file: {e}")
        return 0
    return code


file_path = "/Users/georgiaeick/Library/Mobile Documents/com~apple~TextEdit/Documents/AdventOfCode_Problem11.txt"
file_path_example = "/Users/georgiaeick/Library/Mobile Documents/com~apple~TextEdit/Documents/AdventOfCode_Problem11Ex.txt"


print(readCode(file_path))