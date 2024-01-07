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

races_dict["Time"] = "".join(races_dict["Time"])
races_dict["Distance"] = "".join(races_dict["Distance"])
print(races_dict)

race_times = []
time = int(races_dict["Time"])
distance = int(races_dict["Distance"])
race_times.append(time)
race_times.append(distance)
distances = []
ways_to_beat_record = 0
my_distance = 0
for i in range(time+1):
    my_distance = i*(time-i)
    if my_distance > distance:
        stopp = i
        break

ways_to_win = time+1-2*stopp
print(ways_to_win)