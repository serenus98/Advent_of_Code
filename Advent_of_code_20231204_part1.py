from pathlib import Path

working_directory = Path(__file__).absolute().parent
filename_path = working_directory / "Adventofcode4_1.txt"

def readFile(filePath):
    # reading a file and returning a list of lines
    with open(filePath, 'r') as f:
        return [l.strip() for l in f.readlines()]

cards = readFile(filename_path)
#print(lines_list)
#cards = ["Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53", 
#         "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
 #        "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
 #        "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
 #        "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
  #       "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
  #       ]



def points_of_card(card):    
    result = []
    card = card.replace(":", " |")
    winning_numbers = card.split(" | ")[1].split(" ")
    numbers_you_have = card.split(" | ")[2].split(" ")
    winning_numbers_clean =[]
    numbers_you_have_clean = []
    for number in winning_numbers:
        if number != "":
            winning_numbers_clean.append(number)
    for number in numbers_you_have:
        if number != "":
            numbers_you_have_clean.append(number)
    i = -1
    for number in winning_numbers_clean:
        if number in numbers_you_have_clean:
            i += 1
        if i > -1:
            result = 1*(2**i)
        else:
            result = 0
    return result

points = []
for card in cards:
    points.append(points_of_card(card))
print(sum(points))