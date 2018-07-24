the_file = open("C:\\Users\Marjan\Desktop\\nameslist.txt", "r")
line = the_file.readline()
counter = {}
while line:
    line = line.strip()
    if line in counter:
        counter[line] += 1
    else: 
        counter[line] = 1
    line = the_file.readline()
print(counter)