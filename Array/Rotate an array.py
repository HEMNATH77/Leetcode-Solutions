def rotate(a,k):
    k = k % len(a)
    def reverse(start,end):
        while start < end:
            a[start],a[end] = a[end],a[start]
            start += 1
            end -= 1

    reverse(0,len(a)-1)
    reverse(0,k-1)
    reverse(k,len(a)-1)

a = [1,2,3,4,5,6]
k = 2
rotate(a,k)

print(a)










