def merge_array(num1,num2,m,n):
    p1 = m - 1
    p2 = n - 1
    p = m + n -1
    while p1 >= 0 and p2 >= 0:
        if num1[p1] > num2[p2]:
            num1[p] = num1[p1]
            p1 -= 1
        else:
            num1[p] = num2[p2]
            p2 -= 1
        p -= 1
    while p2 >= 0:
        num1[p] = num2[p2]
        p2 -= 1
        p -= 1


num1 =[1,2,3,0,0,0]
num2 =[2,5,6]
m = 3
n = 3
merge_array(num1,num2,m,n)
print(num1)