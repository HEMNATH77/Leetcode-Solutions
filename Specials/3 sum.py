def three_sum(a):
    a.sort()
    n = len(a)
    result = []

    for i in range(n - 2):
        if i > 0 and a[i] == a[i - 1]:
            continue

        left = i + 1
        right = n - 1

        while left < right:
            total = a[i] + a[left] + a[right]

            if total == 0:
                result.append([a[i],a[left],a[right]])

                while left < right and a[left] == a[left + 1]:
                    left += 1
                while left < right and a[right] == a[right - 1]:
                    right -= 1
                left += 1
                right -= 1

            elif total < 0:
                left += 1
            else:
                right -= 1
    return result

a = [-1,0,1,2,-1,-4]
print(three_sum(a))
