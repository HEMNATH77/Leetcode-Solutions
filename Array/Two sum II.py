def two_sum_II(arr,target):
    n = len(arr)
    left = 0
    right = n - 1
    current_sum = 0

    while(left < right):
        current_sum = arr[left]+ arr[right]

        if current_sum == target:
            return [left+1,right+1]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return []

arr = [2,7,11,15]
target = 9
print(two_sum_II(arr,target))