from pathlib import Path
import regex as re
from math import gcd
from functools import reduce

working_directory = Path(__file__).absolute().parent
filename_path = working_directory / "Adventofcode8.txt"

def readFile(filePath):
    # reading a file and returning a list of lines
    with open(filePath, 'r') as f:
        return [l.strip() for l in f.readlines()]

def next_set_of_keys(keys, side, lines_dict):
    new_keys = []
    for key in keys:
        if side == "R":
            key = lines_dict[key][1]
            new_keys.append(key)
        if side == "L":
            key = lines_dict[key][0]
            new_keys.append(key)
    return new_keys

def lcm_of_list(denominators):
    return reduce(lambda a,b: a*b // gcd(int(a),int(b)), denominators)
#https://stackoverflow.com/users/2868017/takingitcasual

def find_gcd(list):
    x = reduce(gcd, list)
    return x

lines_list = readFile(filename_path)

#print(lines_list)
rl_instructions = lines_list[0]
lines_dict = {}
for i in range(2, len(lines_list)):
    lines_list[i] = lines_list[i].split(" = ")
    lines_dict[lines_list[i][0]] = lines_list[i][1][1:-1].split(", ") 
#print(lines_list)
#print(lines_dict)
#print(rl_instructions)
keys_list = []
for key in lines_dict:
    if key[-1] == "A":
        keys_list.append(key)
#print(keys_list)
counter = 0
condition = []
counters = []
for key in keys_list:
    counter = 0
    while key[-1] != "Z":
        for side in rl_instructions:
            if side == "R":
                key = lines_dict[key][1]
                counter += 1
                #print(key)
            if side == "L":
                key = lines_dict[key][0]
                counter += 1
                #print(key)
    counters.append(counter)
#print(counters)
    
result = find_gcd(counters)
quotient_list = [result]
#print(result)
for counter in counters:
    quotient = counter/result
    quotient_list.append(quotient)
#print(quotient_list)


print(int(lcm_of_list(quotient_list)))