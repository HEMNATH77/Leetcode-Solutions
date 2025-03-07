def remove_duplicates(num):
    if not num:
        return 0
    k = 0
    n = len(num)
    for i in range(1,n):
        if num[i] != num[k]:
            k += 1
            num[k] = num[i]
    return k + 1

a = [1,2,3,2,5,3]
a.sort()
l = remove_duplicates(a)
print(a[:l])