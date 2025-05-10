def array_leaders(s):
    n = len(s)
    l = []
    max = s[-1]
    l.append(max)

    for i in range(n -2,-1,-1):
        if s[i] >= max:
            max = s[i]
            l.append(s[i])
    l.reverse()
    return l
s = [16, 17, 4, 3, 5, 2]
print(array_leaders(s))