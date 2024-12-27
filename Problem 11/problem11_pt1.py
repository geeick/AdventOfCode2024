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


def applyRules(stone):
    result = []
    if int(stone) == 0:
        result = ['1']
    elif len(stone) % 2 == 0:  
        stone1, stone2  = int(stone[:len(stone)//2]), int(stone[len(stone)//2:])
        result = [str(stone1), str(stone2)]
    else:
        result = [str(int(stone)*2024)]
    return result

def blink(code):
    x=0
    while x != len(code):
        results = applyRules(code[x])
        code.pop(x)
        for result in results:
            code.insert(x, result)
            x=x+1
    return code


file_path = "/Users/georgiaeick/Library/Mobile Documents/com~apple~TextEdit/Documents/AdventOfCode_Problem11.txt"
file_path_example = "/Users/georgiaeick/Library/Mobile Documents/com~apple~TextEdit/Documents/AdventOfCode_Problem11Ex.txt"


line = readCode(file_path)

for x in range(25):
    result = (blink(line))
    print(len(result))

