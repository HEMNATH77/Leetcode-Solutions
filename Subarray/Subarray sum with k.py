def longest_subarray(a,k):
    n = len(a)
    maxi = 0
    prefix = 0
    sums = {}

    for i in range(n):
        prefix += a[i]

        if prefix == k in sums:
            maxi = i + 1

        if (prefix - k) in sums:
            maxi = max(maxi,i - sums[prefix - k])

        if prefix not in sums:
            sums[prefix] = i
    return maxi

a = [10,5,2,7,1,-10]
k = 15
print(longest_subarray(a,k))
