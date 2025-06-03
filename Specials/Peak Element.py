def peak_element(arr):
  n = len(arr)
  left = 0 
  right = n - 1
  while left < right:
    mid = (left + right)//2
    if (arr[mid] > arr[mid+1]):
      right = mid
    else:
      left = mid
   return left

arr = [1,2,3,1]
print(peak_element(arr))
