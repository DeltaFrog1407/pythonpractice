#positive.py
def positive(k):
    result = []
    for i in k:
        if i>0:
            result.append(i)
    return result

a = positive([1, -3, 2, 0, -5, 6])

print(a)
