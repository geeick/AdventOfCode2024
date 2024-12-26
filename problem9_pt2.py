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
    fileSize = len(diskMap)
    for x in range (len(diskMap)):
        if diskMap[x][0] != ".":
            nFiles += 1

    seen = {'.'}
    while fileSize > 0:
        if diskMap[fileSize - 1][0] not in seen:
            for x in range (fileSize):
                if diskMap[x][0] == "." and len(diskMap[x]) >= len(diskMap[fileSize-1]):
                    space = []
                    for var in range (len(diskMap[fileSize-1])):
                        temp = diskMap[x][var]
                        diskMap[x][var] = diskMap[fileSize -1][var]
                        diskMap[fileSize- 1][var] = temp
                        seen.add(diskMap[x][0])
                    for var in range (len(diskMap[x])):
                        if diskMap[x][var] == ".":
                            diskMap[x].pop(var)
                            space.append(".")

                    if 1 < fileSize < len(diskMap) and diskMap[fileSize-2][0] == "." and diskMap[fileSize][0] == '.':
                        diskMap[fileSize-2] = diskMap[fileSize-2] + diskMap[fileSize-1] + diskMap[fileSize]
                        diskMap.pop(fileSize)
                        diskMap.pop(fileSize-1)
                    elif 1 < fileSize and diskMap[fileSize-2][0] == ".":
                        diskMap[fileSize-2] = diskMap[fileSize-2] + diskMap[fileSize-1]
                        diskMap.pop(fileSize-1)
                    elif fileSize < len(diskMap) and diskMap[fileSize][0] == '.':
                        diskMap[fileSize-1] = diskMap[fileSize-1] + diskMap[fileSize]
                        diskMap.pop(fileSize)
                    elif len(space) > 0:
                        diskMap.insert(x+1, space)
                    break

            seen.add(diskMap[fileSize-1][0])
        else:
            fileSize -= 1
    return diskMap
                        
def addCheckSum(diskMapArray):
    total = 0
    for x in range (len(diskMapArray)):
        if diskMapArray[x] != ".": 
            total += int(diskMapArray[x]) * x
    return total


file_path = "/Users/georgiaeick/Library/Mobile Documents/com~apple~TextEdit/Documents/AdventOfCode_Problem9.txt"
file_path_example = '/Users/georgiaeick/Library/Mobile Documents/com~apple~TextEdit/Documents/AdventOfCode_Problem9Ex.txt'

file = readDiskMap(file_path_example)
memory = changeMemory(file)
print(addCheckSum(memory))

##not 90273982836 (too low)
    
