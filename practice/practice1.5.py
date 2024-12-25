# reverse a word


def reverse(x):
    y = x.split()
    rev_res = []
    for word in y:
        rev_res.insert(0, word)
    return " ".join(rev_res)


x = input('Enter words: ')
print(reverse(x))
