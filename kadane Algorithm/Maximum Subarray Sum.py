def maximum_subarray(nums):
    n = len(nums)
    maximum = nums[0]
    sum = 0

    for i in nums:
        sum = sum + i
        if sum > maximum:
            maximum = sum
        if sum < 0:
            sum = 0
    return maximum

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maximum_subarray(nums))

