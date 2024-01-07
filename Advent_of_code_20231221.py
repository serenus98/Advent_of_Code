from pathlib import Path

working_directory = Path(__file__).absolute().parent
filename_path = working_directory / "Adventofcode21.txt"

def readFile(filePath):
    # reading a file and returning a list of lines
    with open(filePath, 'r') as f:
        return [l.strip() for l in f.readlines()]

def remove_duplicates(old_list):
    new_list = []
    for old in old_list:
        if old not in new_list:
            new_list.append(old)
    return new_list

def next_garden_field(previous_fields, map):
    garden_fields = []
    for field in previous_fields:
        for i, j in [(field[0]-1,field[1]), (field[0],field[1]-1), 
                    (field[0],field[1]+1), (field[0]+1,field[1])]:
            if map[i][j] in [".", "S"]:
                garden_fields.append([i,j])
    return remove_duplicates(garden_fields)

sketch = readFile(filename_path)
sketch.insert(0, "#"*len(sketch[0]))
sketch.append("#"*len(sketch[0]))

for i in range(len(sketch)):
    sketch[i] = "#"+sketch[i]+"#"

for i in range(len(sketch)):
    for j in range(len(sketch[i])):
        if sketch[i][j] == "S":
            start = [[i,j]]

old_garden_fields = next_garden_field(start, sketch)

for i in range(63):
    new_garden_fields = next_garden_field(old_garden_fields, sketch)
    old_garden_fields = new_garden_fields

print(len(new_garden_fields))


