def sum_circular(nums):
    n = len(nums)

    maximum , current_max = nums[0],nums[0]
    minimum , current_min = nums[0],nums[0]

    total = nums[0]

    for i in range(1,n):
        current_max = max(current_max + nums[i],nums[i])
        maximum = max(maximum,current_max)
        current_min = min(current_min + nums[i], nums[i])
        minimum = min(minimum, current_min)

        total = total + nums[i]

    if maximum > 0: return max(maximum , total - minimum)
    else : return maximum

nums = [1,-2,3,-2]
print(sum_circular(nums))