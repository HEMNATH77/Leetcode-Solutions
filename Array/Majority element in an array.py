def majority(a):
    n = len(a)
    index = 0
    count = 1
    for i in range(1,n):
        if a[i] == a[index]:
            count += 1
        else:
            count -= 1
        if count == 0:
            index = i
            count = 1
    return a[index]

a = [3,2,3]
print(majority(a))













