import re

def processfile(file_path):

    rulesPattern1 = r"(\d+)\|(\d+)"
    rulesPattern2 = r"(\d+)(.*?)(\d+)"
    updatesPattern = r"(\d+)(\n)"    

    try:
        with open(file_path, 'r') as file:
            content = file.read()

            rulesProcessor = re.findall(rulesPattern1, content)     
            updatesProcessor = re.findall(updatesPattern, content)

    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return 0
    except Exception as e:
        print(f"Error reading file: {e}")
        return 0
    
    rules = [(int(a), int(b)) for a, b in rulesProcessor]
    #updates = [list(map(int, line.strip().split(','))) for line in updatesProcessor]

    for line in updatesProcessor:
        if re.findall(rulesPattern2, line):  # Check if 'num' matches the pattern
            print(line)



    print(rules)
    #print(updates)  
            
    

file_path = "/Users/georgiaeick/Library/Mobile Documents/com~apple~TextEdit/Documents/AdventOfCode_Problem5.txt"
file_path_example = '/Users/georgiaeick/Library/Mobile Documents/com~apple~TextEdit/Documents/AdventOfCode_Problem5Ex.txt'
processfile(file_path)