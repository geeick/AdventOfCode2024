def readDiskMap(file_path):
    diskMap = ""
    y = 0
    try:
        with open(file_path, 'r') as file:
            oldDiskMap = [char for char in file.read()]
    
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return 0
    except Exception as e:
        print(f"Error reading file: {e}")
        return 0
    
    for x in range (len(oldDiskMap)):
        if x%2 == 1:
            diskMap += int(oldDiskMap[x]) * "."
        else:
            y = x//2
            diskMap += int(oldDiskMap[x]) * str(y)

    return diskMap

def changeMemory(diskMap):
    diskMapArray = []
    for char in diskMap:
        diskMapArray.append(char)

    arraySize = len(diskMapArray)
    y = arraySize
    spaces = 0

    for x in range (arraySize):
        if diskMapArray[x] == '.':
            spaces += 1

    for x in range (arraySize - spaces):
        if diskMapArray[x] == ".":
            while diskMapArray[y-1] == ".":
                y -= 1
            diskMapArray[x] = diskMapArray[y-1]
            diskMapArray[y-1] = '.'
    
    return diskMapArray
                        
def addCheckSum(diskMapArray):
    total = 0
    for x in range (len(diskMapArray)):
        if diskMapArray[x] != ".": 
            total += int(diskMapArray[x]) * x
    return total


file_path = "/Users/georgiaeick/Library/Mobile Documents/com~apple~TextEdit/Documents/AdventOfCode_Problem9.txt"
file_path_example = '/Users/georgiaeick/Library/Mobile Documents/com~apple~TextEdit/Documents/AdventOfCode_Problem9Ex.txt'

file = readDiskMap(file_path)
memory = changeMemory(file)
print(addCheckSum(memory))

##not 90273982836 (too low)
