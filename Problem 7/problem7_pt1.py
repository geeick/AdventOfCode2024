def processfile(file_path): 

    try: #opening the file
        with open(file_path, 'r') as file:

            lines = file.readlines()

            equations = []

            for line in lines:
                current_solution, current_equation = line.split(":")
                equations.append([current_solution, current_equation])

    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return 0
    except Exception as e:
        print(f"Error reading file: {e}")
        return 0
    return equations

def textToNumbers(text):
    number = []
    numbers = text.strip()
    number = numbers.split(" ")
    for x in range (len(number)):
        number[x] = int(number[x])
    return number

def determineOperators(combinations, iteration):
    operators = []
    for combination in range(combinations):
        options = []
        for index in range(iteration):
            if (combination >> (iteration - index - 1)) & 1:
                options.append("+")  
            else:
                options.append("*") 
        operators.append(options)
    return operators
            
def addOperators(numbers, operators, solution):
    for x in range (len(operators)):   
        total = numbers[0]  
        for y in range(len(numbers) -1):
            if operators[x][y] == ("+"):
                total += numbers[y+1]
            else:
                total *= numbers[y+1]
        if total == int(solution):
            return True
    return False, solution

    
def correct_equation(formula):
    solution, equation = formula
    solution = int(solution)
    if solution == equation:
        return True
            
def run_file(file_path):
    data = processfile(file_path)
    solution = []
    numbers = []
    for x in range (len(data)):
        solution.append(data[x][0])
        number = textToNumbers(data[x][1])
        numbers.append(number)
    total = 0

    for y in range (len(numbers)):
        combinations = pow(2, len(numbers[y]) -1)
        iterations = len(numbers[y]) - 1
        operators = determineOperators(combinations, iterations)
        if addOperators(numbers[y], operators, solution[y]) == True:
            total += int(solution[y])
    print(total)


file_path = "/Users/georgiaeick/Library/Mobile Documents/com~apple~TextEdit/Documents/AdventOfCode_Problem7.txt"
file_path_example = '/Users/georgiaeick/Library/Mobile Documents/com~apple~TextEdit/Documents/AdventOfCode_Problem7Ex.txt'
run_file(file_path)



