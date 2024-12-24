while True:
    age = int(input("Enter your age: "))
    if age >= 17:
        print("You are old enough to drive")
    elif 17 > age > 12:
        print("You are not old enough to drive")
    else:
        print("You are a stupid baby")