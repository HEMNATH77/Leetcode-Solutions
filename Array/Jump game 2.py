def jump2(nums):
    n = len(nums)
    jump  = 0
    last = 0
    current = 0
    for i in range(n-1):
        if i + nums[i] > last:
            last = i + nums[i]
        if i == current:
            jump = jump + 1
            current = last
        if current >= n-1:
            break
    return jump

nums = [2,3,0,1,4]
print(jump2(nums))


