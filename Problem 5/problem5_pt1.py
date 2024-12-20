import re

def processfile(file_path):

    rulesPattern = r"(\d+)|(\d+)" 
    updatesPattern = r"(\d+)"    

    try:
        with open(file_path, 'r') as file:
            content = file.read()

            rules = re.findall(rulesPattern, content)     
            updates = re.findall(updatesPattern, content)

    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return 0
    except Exception as e:
        print(f"Error reading file: {e}")
        return 0


    print(rules)
    #print(updates)  
            
    

file_path = "/Users/georgiaeick/Library/Mobile Documents/com~apple~TextEdit/Documents/AdventOfCode_Problem5.txt"
file_path_example = '/Users/georgiaeick/Library/Mobile Documents/com~apple~TextEdit/Documents/AdventOfCode_Problem5Ex.txt'
print(processfile(file_path))