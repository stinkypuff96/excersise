import random


def first_last():
    return list(random.sample(range(100), 20))


num_l = first_last()
empty_list = []
empty_list.append(num_l[0]), empty_list.append(num_l[-1])
print(num_l)
print(empty_list)

