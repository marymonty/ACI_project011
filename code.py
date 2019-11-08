import random

word_list = []

with open("file.txt") as file:
    for line in file:
    	line = line.strip()
    	word_list.append(line)

poem_str = ""

for x in range(0,5):
	poem_str += word_list[random.randint(0,len(word_list))] + " "
	
print()
print(poem_str)
print()

