def intersection(arr1,arr2):
    a = set(arr1)
    b = set(arr2)

    return list(a&b)

arr1 = [1,2,3,4]
arr2 = [2,4]
print(intersection(arr1,arr2))