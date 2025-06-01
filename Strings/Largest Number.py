def largest_number(nums):
  nums = list(map(str,nums))
  def compare(x,y):
    return (x+y) > (y+x)
  n = len(nums)
  for i in range(n):
    for j in range(0,n - i - 1):
      if not compare(nums[j],nums[j+1]):
        nums[j],nums[j+1] = nums[j+1],nums[j]
  if nums == '0':
    return '0'
  return ''.join(nums)

nums = [10,2]
print(Largest_number(nums))
