def array_diff(a, b):
    for i in b:
        while(a.count(i) > 0):
            a.remove(i)
    return a


a = [1, 2, 3, 4, 5, 4]
b = [1, 2, 4]

print(array_diff(a, b))

