# Create a Fibonacci sequence


def fin_count():
    count = int(input('How many counts would you like to generate: '))
    i = 1
    fib = []
    if count == 0:
        fib = []
    elif count == 1:
        fib = [1]
    elif count == 2:
        fib = [1, 1]
    elif count > 2:
        fib = [1, 1]
    while i < (count - 1):
        fib.append(fib[i] + fib[i - 1])
        i += 1

    return fib


print(fin_count())
input()
