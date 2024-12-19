import re

def checkIfValid(sequence):
    """
    Check if a given sequence is a valid `mul(X,Y)` instruction.
    A valid sequence is of the form `mul(X,Y)` where X and Y are integers (1-3 digits) without spaces.
    """
    pattern = r"^mul\((\d+),(\d+)\)$"
    match = re.match(pattern, sequence)
    return match

def multiplyNumbers(sequence):
    """
    Parse a valid `mul(X,Y)` instruction and return the result of X * Y.
    """
    match = checkIfValid(sequence)
    if match:
        x, y = map(int, match.groups())
        return x * y
    return 0

def processFile(file_path):
    """
    Process the corrupted memory file to extract valid `mul(X,Y)` instructions
    and calculate the total of all multiplication results.
    """
    try:
        with open(file_path, 'r') as file:
            content = file.read()

            # Use regex to find all potential `mul` instructions in the file
            instructions = re.findall(r"mul\(\d+,\d+\)", content)
            
            total = 0
            for instr in instructions:
                if checkIfValid(instr):
                    print(instr)
                    total += multiplyNumbers(instr)

            print(f"Total: {total}")

    except FileNotFoundError:
        print(f"The file at {file_path} does not exist.")
    except IOError:
        print(f"Error reading the file: {file_path}")

# Example usage
# Provide the file path to your corrupted memory file
file_path = "/Users/georgiaeick/Library/Mobile Documents/com~apple~TextEdit/Documents/AdventOfCode_Problem3.txt"
file_path_example = "/Users/georgiaeick/Library/Mobile Documents/com~apple~TextEdit/Documents/AdventOfCode_Problem3Ex.txt"
processFile(file_path)
