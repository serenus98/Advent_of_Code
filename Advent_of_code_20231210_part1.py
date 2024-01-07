from pathlib import Path

working_directory = Path(__file__).absolute().parent
filename_path = working_directory / "Adventofcode10.txt"

def readFile(filePath):
    # reading a file and returning a list of lines
    with open(filePath, 'r') as f:
        return [l.strip() for l in f.readlines()]

sketch = readFile(filename_path)

for i in range(len(sketch)):
    for j in range(len(sketch[i])):
        if sketch[i][j] == "S":
            print("starting point at: ", i, j)

current_x = i
current_y = j
current_symbol = sketch[i][j]
prev_x = i
prev_y = j

def next_pos(prev_x, prev_y, current_symbol, current_x, current_y, sketch):
    if current_symbol == "S":
        for i in range(prev_x-1, prev_x+1):
            for j in range(prev_y-1, prev_y+1):
                if sketch[i][j] in ["J", "|", "-", "7", "L", "F"]:
                    prev_x = current_x
                    prev_y = current_y
                    current_symbol = sketch[i][j]
                    current_x = i
                    current_y = j    
                if current_symbol == "|":
                    if prev_x == current_x-1:
                        prev_x = current_x
                        prev_y = current_y
                        next_x = current_x + 1
                        next_y = current_y
        #if prev_x == current_x+1:
         #   prev_x = current_x
          #  prev_y = current_y
           # next_x = current_x - 1
            #next_y = current_y
#if current_symbol == "-":
#    prev_x = current_x
#    prev_y = current_y
#    current_x += 1
#    current_y = current_y
#if current_symbol == "L":
#    prev_x = current_x
#    prev_y = current_y
#    current_x += 1
#    current_y = current_y
#if current_symbol == "F":
#    prev_x = current_x
#    prev_y = current_y
#    current_x += 1
#    current_y = current_y
#if current_symbol == "7":
#    prev_x = current_x
#    prev_y = current_y
#    current_x += 1
#    current_y = current_y
#if current_symbol == "J":
#    prev_x = current_x
#    prev_y = current_y
#    current_x += 1
#    current_y = current_y
    
    
    return [next_x, next_y]

print(next_pos(prev_x, prev_y, current_symbol, current_x, current_y, sketch))