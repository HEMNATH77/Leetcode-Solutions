def container_with_most_water(arr):
    n = len(arr)
    left = 0
    right = n - 1
    max_sum = 0

    for i in range(n):
        h = min(arr[left],arr[right])
        w = right - left
        area = h * w
        max_sum = max(max_sum,area)

        if arr[left] < arr[right]:
            left += 1
        else:
            right -= 1
    return max_sum

arr = [1,8,6,2,5,4,8,3,7]
print(container_with_most_water(arr))