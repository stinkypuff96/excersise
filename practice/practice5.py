# Remove duplicates from list

a = [1, 1, 2, 4, 5, 5, 6, 6, 7, 7, 6, 7, 2, 3, 9]
b = []


def no_repeat():
    return


for i in a:
    if i not in b:
        b.append(i)

print(b)