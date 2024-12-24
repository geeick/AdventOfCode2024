import re
from collections import defaultdict

def processfile(file_path): 

    rulesPattern = r"(\d+)\|(\d+)"  #defining patterns
    updatesPattern = r"(\d+)"    

    try: #opening the file
        with open(file_path, 'r') as file:
            content = file.read()

            rules_part, updates_part = content.split("\n\n") #content is split into rules part and updates part when there is a double new line

            rulesProcessor = re.findall(rulesPattern, rules_part) #the rules part follows the rulesPattern
            
            #removes whitespace characters
            #divide into list of substrings
            #for each substring separate values in list by comma
            #"map" converts each element into an intager
            #"list" converts the map result into a list
            #final result is a 2d list of intagers
            #ex: from updates_part = """1, 2, 3,  to updatesProcessor = [[1, 2, 3],
            #                           4, 5, 6,                           [4, 5, 6],
            #                           7, 8, 9"""                         [7, 8, 9]]
            
            updatesProcessor = [list(map(int, update.split(','))) for update in updates_part.strip().split("\n")]

    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return 0
    except Exception as e:
        print(f"Error reading file: {e}")
        return 0
    

    def make_graph(update):
        graph = defaultdict(set)  #making graph to store values. defaultdict(set) makes default keys for value that don't exist
        in_degree = defaultdict(int) #counts the number of edges directed towards a node

        all_pages = set(update)  # Use only pages from the current update
        filtered_rules = [rule for rule in rulesProcessor if int(rule[0]) in all_pages and int(rule[1]) in all_pages]

        for rule in filtered_rules:
            X, Y = map(int, rule)
            #only add the rule to the graph if both X and Y are in the current update
            graph[X].add(Y)
            in_degree[Y] += 1
        
        # If a page has no in_degrees, make in degree of zero
        for page in all_pages:
            if page not in in_degree:
                in_degree[page] = 0
        
        return graph, in_degree


    def is_valid_update(update):
        graph, in_degree = make_graph(update)  #create the graph for this specific update
        seen = set() #make a set to keep track of pages already seen
        for i in range(len(update)):
            current_page = update[i]
            for previous_page in seen: #if the current page was supposed to come before a previous_page then the update is invalid
                if current_page in graph and previous_page in graph[current_page]:
                    temp = update[i]
                    update[i] = update[i-1]
                    update[i-1] = temp
                    return False
            seen.add(current_page)
        return True
    
    valid_middle_sum = 0

    for update in updatesProcessor: #if a update is valid, add it's middle value
        if is_valid_update(update) == False:
            while is_valid_update(update) == False:
                is_valid_update(update)
            mid_index = len(update) // 2
            middle_page = update[mid_index]
            valid_middle_sum += middle_page
            print(middle_page)
    
    return valid_middle_sum
            
    
file_path = "/Users/georgiaeick/Library/Mobile Documents/com~apple~TextEdit/Documents/AdventOfCode_Problem5.txt"
file_path_example = '/Users/georgiaeick/Library/Mobile Documents/com~apple~TextEdit/Documents/AdventOfCode_Problem5Ex.txt'

result = processfile(file_path)
print(f"Sum of middle pages: {result}")
