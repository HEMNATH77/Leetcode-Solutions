def anagram(s:str,t :str):
    if len(s) != len(t):
        return False
    c1 = {}                              #c1,c2 = count
    c2 = {}
    for i in s:
        if i in c1:
            c1[i] += 1
        else:
            c1[i] = 1
    for i in t:
        if i in c2:
            c2[i] += 1
        else:
            c2[i] = 1
    return c1 == c2

s = "ANAGRAM"
t = "NAGARAM"

print(anagram(s,t))
