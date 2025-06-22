def group_reverse(arr,k):
    n = len(arr)

    for i in range(0,n,k):
        left = i
        right = min(i + k - 1, n -1)

        while(left < right):
            arr[left],arr[right] = arr[right],arr[left]
            left += 1
            right -= 1
    return arr

arr =[1, 2, 3, 4, 5]
k = 3
print(group_reverse(arr,k))
