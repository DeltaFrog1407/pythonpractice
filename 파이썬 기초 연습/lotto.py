import random

def lotto(a):
    number = random.randint(0, 44)
    return data.pop(number)

data = list(range(1, 46))
count = 1
while count:
    print(lotto(data))
    count += 1
    if count == 7:
        break
