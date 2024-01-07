from pathlib import Path

working_directory = Path(__file__).absolute().parent
filename_path = working_directory / "Adventofcode6_1.txt"

def readFile(filePath):
    # reading a file and returning a list of lines
    with open(filePath, 'r') as f:
        return [l.strip() for l in f.readlines()]

lines_list = readFile(filename_path)

print(lines_list)

races_dict = {}
numbers_clean = []
for line in lines_list:
    for number in line.split(":")[1].split(" "):
        if number != "":
            numbers_clean.append(number)
    races_dict[line.split(":")[0]] = numbers_clean
    numbers_clean = []

print(races_dict)

race_times = []
all_ways = []
for i in range(len(races_dict["Time"])):
    time = int(races_dict["Time"][i])
    distance = int(races_dict["Distance"][i])
    race_times.append(time)
    race_times.append(distance)
    distances = []
    for i in range(time):
        distances.append(i*(time-i))
        ways_to_beat_record = 0
    for my_distance in distances:
        if my_distance > distance:
            ways_to_beat_record += 1
    all_ways.append(ways_to_beat_record)
print(all_ways)

def multiply_list(all_ways):
    result = 1
    for number in all_ways:
        result *= int(number)
    return result

print(multiply_list(all_ways))