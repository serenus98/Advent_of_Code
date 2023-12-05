from pathlib import Path
import regex as re

working_directory = Path(__file__).absolute().parent
filename_path = working_directory / "Adventofcode2_1.txt"

def readFile(filePath):
    # reading a file and returning a list of lines
    with open(filePath, 'r') as f:
        return [l.strip() for l in f.readlines()]

lines_list = readFile(filename_path)
#print(lines_list)

colours = {"blue": 0, "green": 0, "red": 0}
games = {}
split_lines_list = []

for line in lines_list:
    split_lines_list.append(line.split(": "))
#print(split_lines_list)

for line in split_lines_list:
     games[int(line[0].split(" ")[1])] = line[1].replace("; ", ", ")
     games[int(line[0].split(" ")[1])] = games[int(line[0].split(" ")[1])].split(", ")
#print(games)

trial = []
for key in games:
    #print(key)
    for item in games[key]:
        #print(item)
        item = item.split(" ")
        #print(item)
        if item[1] == "red":
            if int(item[0]) > 12:
                games[key] = "impossible"
        if item[1] == "blue":
            if int(item[0]) > 14:
                games[key] = "impossible"
        if item[1] == "green":
            if int(item[0]) > 13:
                games[key] = "impossible"
#print(games)

result = 0

for key in games:
    if games[key] != "impossible":
        result += key
print(result)


    #pattern = r"[0-9]{1,} blue|[0-9]{1,} green|[0-9]{1,} red"
    #game_list = re.findall(pattern, str(games[key]))
    #trial.append(game_list)
#print(trial)    

#for i in range(len(trial)):
#    games[i+1] = "".join(trial[i])
#print(games)

blue_game_list = []
green_game_list = []
red_game_list = []
for j in range(1,len(games)):
    #print(j)
    if "blue" in str(games[j]):
        temp_game_list = re.findall(r"[0-9]{1,} blue", str(games[j]))
        blue_game_list.extend(temp_game_list)
        #print(j)
    if "green" in str(games[j]):
        temp_game_list = re.findall(r"[0-9]{1,} green", str(games[j]))
        green_game_list.extend(temp_game_list)
        #print(j)
    if "red" in str(games[j]):
        temp_game_list = re.findall(r"[0-9]{1,} red", str(games[j]))
        red_game_list.extend(temp_game_list)
        #print(j)
#print(blue_game_list)
#print(green_game_list)
#print(red_game_list)

digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
blue_list = []
green_list = []
red_list = []
for cube in blue_game_list:
    blue_list.append(cube.split(" ")[0])
for cube in green_game_list:
    green_list.append(cube.split(" ")[0])
for cube in red_game_list:
    red_list.append(cube.split(" ")[0])
#print(blue_list)
#print(green_list)
#print(red_list)
#print(games[j])