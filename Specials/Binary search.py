def binary_search(a,target):
    n = len(a)

    left = 0
    right = n - 1

    while left <= right:
        mid = (left + right) // 2

        if a[mid] == target:
            return mid
        elif a[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return  -1

a = [-1,0,2,4,6,8,9]
target= 9
print(binary_search(a,target))


