from pathlib import Path

working_directory = Path(__file__).absolute().parent
filename_path = working_directory / "Adventofcode10.txt"

def readFile(filePath):
    # reading a file and returning a list of lines
    with open(filePath, 'r') as f:
        return [l.strip() for l in f.readlines()]

sketch = readFile(filename_path)
sketch_copy = readFile(filename_path)

for i in range(len(sketch_copy)):
    sketch_copy[i] = len(sketch_copy[i])*"."

print(sketch_copy)
print(sketch)
def find_start(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == "S":
                #print("starting point at: ", i, j)
                start_x = i
                start_y = j
    return start_x, start_y

def find_first_tube(abscisse, ordonnee):
    if sketch[ordonnee-1][abscisse] in ["|", "7", "F"]: 
        return sketch[ordonnee-1][abscisse], ordonnee-1, abscisse
    if sketch[ordonnee][abscisse-1] in ["-", "L", "F"]: 
        return sketch[ordonnee][abscisse-1], ordonnee, abscisse-1
    if sketch[ordonnee][abscisse+1] in ["J", "-", "7"]: 
        return sketch[ordonnee][abscisse+1], ordonnee, abscisse+1
    if sketch[ordonnee+1][abscisse] in ["J", "|", "L"]: 
        return sketch[ordonnee+1][abscisse], ordonnee+1, abscisse        
    
def next_position(prev_x, prev_y, current_x, current_y, current_symbol):
    global next_x
    global next_y
    if current_symbol == "|":
        if prev_x == current_x-1:
            next_x = current_x+1
            next_y = current_y
            prev_x = current_x
            prev_y = current_y
            current_x = next_x
            current_y = next_y
        elif prev_x == current_x+1:
            next_x = current_x-1
            next_y = current_y
            prev_x = current_x
            prev_y = current_y
            current_x = next_x
            current_y = next_y
    if current_symbol == "-":
        if prev_y == current_y+1:
            next_x = current_x
            next_y = current_y-1
            prev_x = current_x
            prev_y = current_y
            current_x = next_x
            current_y = next_y
        elif prev_y == current_y-1:
            next_x = current_x
            next_y = current_y+1
            prev_x = current_x
            prev_y = current_y
            current_x = next_x
            current_y = next_y
    if current_symbol == "F":
        if prev_x == current_x:
            next_x = current_x+1
            next_y = current_y
            prev_x = current_x
            prev_y = current_y
            current_x = next_x
            current_y = next_y
        elif prev_y == current_y:
            next_x = current_x
            next_y = current_y+1
            prev_x = current_x
            prev_y = current_y
            current_x = next_x
            current_y = next_y
    if current_symbol == "L":
        if prev_x == current_x:
            next_x = current_x-1
            next_y = current_y
            prev_x = current_x
            prev_y = current_y
            current_x = next_x
            current_y = next_y
        elif prev_y == current_y:
            next_x = current_x
            next_y = current_y+1
            prev_x = current_x
            prev_y = current_y
            current_x = next_x
            current_y = next_y
    
    return next_x, next_y, current_x, current_y, current_symbol

prev_x = find_start(sketch)[0]
prev_y = find_start(sketch)[1]
current_x = find_first_tube(prev_x,prev_y)[1] 
current_y = find_first_tube(prev_x,prev_y)[2]  
current_symbol = find_first_tube(prev_x,prev_y)[0]
print("start_x: ", prev_x)
print("start_y: ", prev_y)
print("current_x: ", current_x)
print("current_y: ", current_y)  
print("current_symbol: ", current_symbol)
positions = []
for i in range(5):
    positions.append(next_position(prev_x, prev_y, current_x, current_y, current_symbol))
    next_step = next_position(prev_x, prev_y, current_x, current_y, sketch[current_x][current_y])
    prev_x = next_step[0]
    prev_y = next_step[1]
    current_x = next_step[2]
    current_y = next_step[3] 
    current_symbol = next_step[4]
    print(current_symbol)
print(positions)