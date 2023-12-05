from pathlib import Path
import regex as re

working_directory = Path(__file__).absolute().parent
filename_path = working_directory / "Adventofcode2.txt"

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

blue_game_list = []
green_game_list = []
red_game_list = []

for key in games:
    for item in games[key]:
        #print(item)
        item = item.split(" ")
        #print(item)
        if item[1] == "red":
            red_game_list.append(int(item[0]))
        if item[1] == "blue":
            blue_game_list.append(int(item[0]))
        if item[1] == "green":
            green_game_list.append(int(item[0]))
    games[key] = [max(blue_game_list)*max(green_game_list)*max(red_game_list), ]
    blue_game_list = []
    green_game_list = []
    red_game_list = []
    #print(blue_game_list)
    #print(green_game_list)
    #print(red_game_list)
    #print(games)
result = 0
for key in games:
    result += int(games[key][0])
print(result)