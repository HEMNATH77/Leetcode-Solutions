def index(s,t):
    n = len(s)
    m = len(t)
    for i in range(n - m + 1):
        match = True
        for j in range(m):
            if s[i+j] != t[j]:
                match = False
                break
        if match:
            return  i
    return  -1

s = "sadbutsad"
t = "sad"

print(index(s,t))


