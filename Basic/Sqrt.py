def sqrt(a):
  if a < 2:
    return a
  low = 1
  high = a

  while low <= high:
    mid = (low + high) // 2
    if mid * mid == a:
      return mid
    elif mid * mid < a:
      low = mid + 1
      ans = low
    else:
      high = mid - 1
  return ans

a = 9
print(sqrt(a))
