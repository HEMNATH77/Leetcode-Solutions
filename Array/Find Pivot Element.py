def pivot_element(nums):
    n = len(nums)
    left = 0
    right = 0

    for a in nums:
        right = right + a
    for i in range(0,n):
        right = right - nums[i]
        if (left == right):
            return i
        else:
            left = left + nums[i]
    return -1

nums = [1,7,3,6,5,6]
print(pivot_element(nums))