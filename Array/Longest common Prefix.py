def long(s):
    if not s:
        return ""
    for i in range(len(s[0])):
        char = s[0][i]
        for j in s[1:]:
            if i >= len(j) or j[i] != char:
                return s[0][:i]
    return s[0]

s = ["blow","blue","bless"]
print(long(s))

