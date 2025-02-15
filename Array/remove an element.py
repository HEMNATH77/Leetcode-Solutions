def remove(a,e):
    k = 0
    for i in range(len(a)):
        if a[i]!= e:
            a[k] = a[i]
            k += 1
    return k

a = [1,2,3,2,4]
e = 2
print(remove(a,e))

