from pathlib import Path

working_directory = Path(__file__).absolute().parent
filename_path = working_directory / "Adventofcode9_1.txt"

def readFile(filePath):
    # reading a file and returning a list of lines
    with open(filePath, 'r') as f:
        return [l.strip() for l in f.readlines()]

def predict_next(numbers_list, last_pos):                               #function to do the pairwise subtraction and save the last difference
    #two arguments: list of numbers (str) and last_position as list --> important for recursion!
    diff_list = []                                                      #initiate diff_list
    for i in range(len(numbers_list)-1):                                #loop that iterates through a list of numbers
        difference = int(numbers_list[i+1])-int(numbers_list[i])        #difference of two adjacent numbers in the list
        diff_list.append(difference)                                    #saving the differences in a list called diff_list
    last_pos.append(diff_list[-1])                                      #saving the last position of the differences list in another list
    if sum(diff_list) != 0:                                             #checks if all elements of a list are 0
        predict_next(diff_list,last_pos)                                #if not a new recursion (function calls itself) is initiated 
    return sum(last_pos)                                                #the function returns the sum of all the elements in the last_position list

lines_list = readFile(filename_path)                                    #the file is read. returns a list of lines as String
result = 0                                                              #result is initiated as 0 (int)
for line in lines_list:                                                 #this loop iterates through all the lines of the input file
    line = line.split(" ")                                              #line is defined as a list of elements previously separated by a space(" ") in the string
    last_pos = [int(line[-1])]                                          #the last position is defined as the last element of the line list
    result += predict_next(line, last_pos)                              #the final result is the sum of the predictions from each line

print(result)                                                           #prints the final result to the terminal