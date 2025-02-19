def reverse(s):
    words = []
    w = ""
    for i in s:
        if i != " ":
            w += i
        else:
            if w:
                words.append(w)
                w = ""
    if w:
        words.append(w)
    rev = ""
    for i in range(len(words) -1,-1,-1):
        rev += words[i]
        if i != 0:
            rev += " "
    return rev

s = "Hello World"
print(reverse(s))

