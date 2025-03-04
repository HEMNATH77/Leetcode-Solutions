def two_sums(num):
    n = len(num)
    for i in range(n):
        for j in range(i + 1,n):
            if num[i] + num[j] == target:
                return[i,j]
    return[]

num = [2,4,6,7,8,9]
target = 9
print(two_sums(num))
