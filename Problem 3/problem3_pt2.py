import re

def processFile(file_path):
    mul_pattern = r"mul[\[\(](\d+),(\d+)[\]\)]" 
    do_pattern = r"do\(\)"                      
    dont_pattern = r"don't\(\)"                 
    enabled = True
    total_sum = 0

    try:
        with open(file_path, 'r') as file:
            memory = file.read()
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return 0
    except Exception as e:
        print(f"Error reading file: {e}")
        return 0

    combined_pattern = f"{mul_pattern}|{do_pattern}|{dont_pattern}"
    instructions = re.finditer(combined_pattern, memory)
    
    for match in instructions:
        if match.group(1) and match.group(2):
            if enabled:
                total_sum += int(match.group(1)) * int(match.group(2))
        elif match.group(0) == "do()": 
            enabled = True
        elif match.group(0) == "don't()": 
            enabled = False

    return total_sum

file_path = "/Users/georgiaeick/Library/Mobile Documents/com~apple~TextEdit/Documents/AdventOfCode_Problem3.txt"
file_path_example = '/Users/georgiaeick/Library/Mobile Documents/com~apple~TextEdit/Documents/AdventOfCode_Problem3Ex.txt'
print(processFile(file_path))




