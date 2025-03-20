def jump1(nums):
    n = len(nums)
    last = 0
    for i in range(n):
        if i > last:
            return False
        if i + nums[i] > last:
            last = i + nums[i]
    else:
        return True
nums = [3,2,1,0,4]
print(jump1(nums))