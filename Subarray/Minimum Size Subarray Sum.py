def minimum_size_subarray_sum(arr,target):
    n = len(arr)
    left = 0
    total = 0
    min_sum = n + 1

    for i in range(n):
        total = total + arr[i]

        while total >= target:
            min_sum = min(min_sum,i - left + 1)
            total = total - arr[left]
            left += 1
    if min_sum == n + 1:
        return 0
    else:
        return min_sum

arr = [2,3,1,2,4,3]
target = 7
print(minimum_size_subarray_sum(arr, target))
