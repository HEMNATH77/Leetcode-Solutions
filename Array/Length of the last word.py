def last_word(a):
    length  = 0
    i = len(a) - 1
    while i >= 0 and a[i] == ' ':
        i -=1
    while i >= 0 and a[i] != ' ' :
        length +=1
        i -= 1
    return length

a = "Hello World"
print(last_word(a))



