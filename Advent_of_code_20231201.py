
from pathlib import Path

working_directory = Path(__file__).absolute().parent
filename_path = working_directory / "Adventofcode1.txt"

def readFile(filePath):
    # reading a file and returning a list of lines
    with open(filePath, 'r') as f:
        return [l.strip() for l in f.readlines()]

lines_list = readFile(filename_path)
print(lines_list)

digits = ["0","1","2","3","4","5","6","7","8","9"]
temp = []
result = []
for line in lines_list:
    for char in line:
        if char in digits:
            temp.append(char)
    result.append(temp[0] + temp[-1])
    temp = []

print(result)

digit_sum = 0
for digit in result:
    digit_sum += int(digit)
print(digit_sum)





#code = "smfjh3njhg5ur4hjks"
#digits = ["0","1","2","3","4","5","6","7","8","9"]
#solution = []
#for char in code:
#    if char in digits:
#        solution.append(char)
#result = solution[0] + solution[-1]
#print(result)

