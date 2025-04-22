def Number_1(a):
    count = 0
    while(n):
       count += a & 1
       a >>= 1
    return count
a = int('1001')
print(Number_1(a))
