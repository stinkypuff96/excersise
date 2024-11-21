import random

a = random.sample(range(100), 15)
b = random.sample(range(100), 20)
print('This is group A:', a)
print('This is group B:', b)

print('These are the common numbers:', [i for i in b if i in a])
