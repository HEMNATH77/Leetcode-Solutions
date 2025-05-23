def closet(arr,target):
    arr.sort()
    n = len(arr)

    close = arr[0]+arr[1]+arr[2]
    min_diff = close - target

    if min_diff < 0 :
        min_diff = -min_diff

    for i in range(n - 2):
        left = i + 1
        right = n - 1

        while left < right:
            current = arr[i]+arr[left]+arr[right]
            diff = current - target

            if diff < 0:
                if -diff < min_diff:
                    min_diff = -diff
                    close = current
                elif -diff == min_diff and current > close:
                    close = current
                left +=1
            elif diff > 0:
                if diff < min_diff:
                    min_diff = diff
                    close = current
                elif diff == min_diff and current > close:
                    close = current
                right -= 1
            else:
                return current
    return close

arr = [-1,2,1,-4]
target = 1
print(closet(arr,target))



