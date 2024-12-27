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

def blink(stone, blinks, key, cache):
    result = 0
    total = 0

    if key in cache:
        result = cache[key]
    else:
        if blinks == 0:
            result = 1
        else:
            for stones in applyRules(stone):
                total += blink(stones, blinks -1, (stones, blinks -1), cache)
            cache[key] = total
            result = cache[key]

    return result


def countStones(stones, x):
    cache = {}
    total = 0  
    
    for stone in stones:
        total += blink(stone, x, (stone, x), cache)
    
    return total

file_path = "/Users/georgiaeick/Library/Mobile Documents/com~apple~TextEdit/Documents/AdventOfCode_Problem11.txt"
file_path_example = "/Users/georgiaeick/Library/Mobile Documents/com~apple~TextEdit/Documents/AdventOfCode_Problem11Ex.txt"


line = readCode(file_path)

result = line

print(countStones(result, 75))

