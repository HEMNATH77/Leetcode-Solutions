def longest_substring(s):
    n = len(s)
    result = []
    max_sum = 0

    for i in range(n):
        result = []
        for j in range(i,n):
            if s[j] not in result:
                result.append(s[j])
            else:
                break
        max_sum = max(max_sum,len(result))
    return max_sum

s = "abcabcbb"
print(longest_substring(s))