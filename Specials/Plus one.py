def plus_one(a):
    n = len(a)
    for i in range(n - 1, -1, -1):
        if a[i] < 9:
            a[i] += 1
            return a
        a[i] = 0
    return [1] + a
a = [9,9,9]
print(plus_one(a))