from pathlib import Path
import time
start_time_1 = time.process_time_ns()
working_directory = Path(__file__).absolute().parent
filename_path = working_directory / "Adventofcode8.txt"

def readFile(filePath):
    # reading a file and returning a list of lines
    with open(filePath, 'r') as f:
        return [l.strip() for l in f.readlines()]

lines_list = readFile(filename_path)

#print(lines_list)
rl_instructions = lines_list[0]
lines_dict = {}
for i in range(2, len(lines_list)-1):
    lines_list[i] = lines_list[i].split(" = ")
    lines_dict[lines_list[i][0]] = lines_list[i][1][1:-1].split(", ") 
#print(lines_list)
#print(lines_dict)
#print(rl_instructions)
key = "AAA"
counter = 0
while key != "ZZZ":
    for char in rl_instructions:
        if char == "R":
            key = lines_dict[key][1]
            counter += 1
            #print(key)
        if char == "L":
            key = lines_dict[key][0]
            counter += 1
            #print(key)
print(counter)
start_time_2 = time.process_time_ns()
dauer = start_time_2-start_time_1
print(dauer)