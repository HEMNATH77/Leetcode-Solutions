def remove_duplicates(num):
    if len(num) < 2:
        return len(num)
    k = 1
    count = 1
    for i in range(1,len(num)):
        if num[i] == num[i - 1]:
            count += 1
        else:
            count = 1

        if count <= 2:
            k += 1
            num[k - 1] = num[i]
    return k

a = [1,2,2,3,2,1,3,5]
a.sort()
l = remove_duplicates(a)
print(a[:l])
