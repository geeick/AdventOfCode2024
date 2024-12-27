def readDiskMap(file_path):
    diskMap = []
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
        subDisk = []
        if oldDiskMap[x] == '0':
            continue
        for z in range (int(oldDiskMap[x])):
            if x%2 == 1:
                subDisk.append('.')
            else:
                y = x//2
                subDisk.append(str(y))
        diskMap.append(subDisk)

    return diskMap



def changeMemory(diskMap):
    nFiles = 0
    fileModified = len(diskMap) -1
    for x in range (len(diskMap)):
        if diskMap[x][0] != ".":
            nFiles += 1

    seen = {'.'}
    while fileModified > 0:
        if diskMap[fileModified][0] not in seen:
            for x in range (fileModified):
                seen.add(diskMap[fileModified][0])
                if diskMap[x][0] == "." and len(diskMap[x]) >= len(diskMap[fileModified]):
                    space = []
                    for var in range (len(diskMap[fileModified])):
                        temp = diskMap[x][var]
                        diskMap[x][var] = diskMap[fileModified][var]
                        diskMap[fileModified][var] = temp
                        seen.add(diskMap[x][0])
                    for var in range (len(diskMap[x]) -1, -1, -1):
                        if diskMap[x][var] == ".":
                            space.append(".")
                            diskMap[x].pop(var)

                    if 0 < fileModified < len(diskMap) - 1 and diskMap[fileModified-1][0] == "." and diskMap[fileModified +1][0] == '.':
                        diskMap[fileModified-1] = diskMap[fileModified-1] + diskMap[fileModified] + diskMap[fileModified +1]
                        diskMap.pop(fileModified +1)
                        diskMap.pop(fileModified)
                        fileModified -= 2
                    elif 1 <= fileModified and diskMap[fileModified -1][0] == ".":
                        diskMap[fileModified -1] = diskMap[fileModified-1] + diskMap[fileModified]
                        diskMap.pop(fileModified)
                        fileModified -= 1
                    elif fileModified  < len(diskMap) -1 and diskMap[fileModified +1][0] == '.':
                        diskMap[fileModified] = diskMap[fileModified] + diskMap[fileModified +1]
                        diskMap.pop(fileModified)
                        fileModified -= 1

                    if len(space) > 0:
                        diskMap.insert(x+1, space)
                        fileModified += 1
                    break
        else:
            fileModified -= 1
    return diskMap
                        
def addCheckSum(diskMapArray):
    total = 0
    diskArray = []
    rows = len(diskMapArray)
    for row in range(rows):
        cols = len(diskMapArray[row])
        for col in range (cols):
            diskArray.append(diskMapArray[row][col])

    for x in range (len(diskArray)):
        if diskArray[x] != ".": 
            add = int(diskArray[x]) * x
            total += add
            
    return total


file_path = "/Users/georgiaeick/Library/Mobile Documents/com~apple~TextEdit/Documents/AdventOfCode_Problem9.txt"
file_path_example = '/Users/georgiaeick/Library/Mobile Documents/com~apple~TextEdit/Documents/AdventOfCode_Problem9Ex.txt'

file = readDiskMap(file_path)
memory = changeMemory(file)
print(addCheckSum(memory))

#6372379482458 is too low
