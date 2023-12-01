from pathlib import Path
import regex as re

working_directory = Path(__file__).absolute().parent
filename_path = working_directory / "Adventofcode1.txt"

def readFile(filePath):
    # reading a file and returning a list of lines
    with open(filePath, 'r') as f:
        return [l.strip() for l in f.readlines()]

lines_list = readFile(filename_path)
print(lines_list)

digits = ["0","1","2","3","4","5","6","7","8","9"]
numerals = ["0","1","2","3","4","5","6","7","8","9","zero","one","two","three","four","five","six","seven","eight","nine"]
temp = ""
result = []
translate = {"zero":"0",
             "one":"1",
             "two":"2",
             "three":"3",
             "four":"4",
             "five":"5",
             "six":"6",
             "seven":"7",
             "eight":"8",
             "nine":"9"}

lines_list_new = []
matchlist = []
for line in lines_list:
    for i in range(len(line)):
        for j in range(len(line)+1):
            #print(line[i:j])
            for element in numerals:
                if element == line[i:j]:
                    matchlist.append(element)
    result.append(matchlist)
    matchlist = []
print(result)

for list in result:
    for i in range(len(list)):
        if list[i] in translate:
            list[i] = translate[list[i]]
print("result: ", result)

#digits = ["0","1","2","3","4","5","6","7","8","9"]
#temp = []
final = []
for list in result:
    final.append(list[0] + list[-1])
print(final)  

#print(result)

digit_sum = 0
for digit in final:
    digit_sum += int(digit)
print(digit_sum)