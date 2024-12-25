# read from file

name_count = {}

with open('names.txt', 'r') as open_file:
    all_text = open_file.readline()

    while all_text:
        all_text = all_text.strip()
        if all_text in name_count.keys():
            name_count[all_text] += 1
        else:
            name_count[all_text] = 1
        all_text = open_file.readline()

print(name_count)
