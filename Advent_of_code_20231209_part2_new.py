from pathlib import Path

working_directory = Path(__file__).absolute().parent
filename_path = working_directory / "Adventofcode9_1.txt"

def readFile(filePath):
    # reading a file and returning a list of lines
    with open(filePath, 'r') as f:
        return [l.strip() for l in f.readlines()]

def predict_next(numbers_list, last_pos, first_pos):                               
    diff_list = []  
    new_diff_list = [0]                                                    
    for i in range(len(numbers_list)-1):                                
        difference = int(numbers_list[i+1])-int(numbers_list[i])        
        diff_list.append(difference)                                      
    last_pos.insert(0,diff_list[0])
    #print("last_pos", last_pos)  
    for i in range(len(last_pos)-1):                                
        difference = int(last_pos[i+1])-int(new_diff_list[i])        
        new_diff_list.append(difference)
        #print("new_diff_list: ", new_diff_list) 
        first_pos.append(new_diff_list[-1])
    #print("first_pos: ", first_pos)                                   
    if sum(diff_list) != 0:
        #print("first_pos2: ", first_pos)                                             
        predict_next(diff_list,last_pos, first_pos)
        #print("first_pos3: ", first_pos)
    return first_pos[-1]               

lines_list = readFile(filename_path)                                    
result = [] 
for line in lines_list:                                                 
    line = line.split(" ")                                              
    last_pos = [int(line[0])]                                          
    result.append(predict_next(line, last_pos, []))
#print(result)
print(sum(result))