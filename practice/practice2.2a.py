name_count = {}

with open('categories.txt', 'r') as open_file:
    line = open_file.readline()
    while line:
        line = line[3: -26]
        if line in name_count:
            name_count[line] += 1
        else:
            name_count[line] = 1
        line = open_file.readline()

print(name_count)